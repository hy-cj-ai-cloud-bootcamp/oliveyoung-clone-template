"""
올리브영 AI 뷰티 어드바이저 - Streamlit 챗봇 UI

[Day3 구현 가이드]
AWS Bedrock을 활용한 AI 챗봇입니다.

구현 완료 후 흐름:
1. 사용자가 뷰티 관련 질문 입력
2. 백엔드가 DB에서 상품 데이터를 조회하여 프롬프트 컨텍스트 생성
3. Bedrock FM(Claude)이 답변 생성 → 화면에 표시

접속 주소: http://localhost:8501
"""
import streamlit as st
import requests
import os

st.set_page_config(
    page_title="올리브영 AI 뷰티 어드바이저",
    page_icon="🫒",
    layout="centered"
)

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

st.title("🫒 올리브영 AI 뷰티 어드바이저")
st.markdown("AWS Bedrock 기반 AI가 피부 타입, 예산, 고민에 맞는 제품을 추천해드립니다!")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 올리브영 AI 뷰티 어드바이저입니다. 🫒\n\n어떤 제품을 찾으시나요?\n\n예시:\n- 건성 피부에 좋은 수분크림 추천해줘\n- 1만원 이하 립스틱 보여줘\n- 여드름 피부에 좋은 제품 있어?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("뷰티 관련 질문을 입력하세요..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("추천 상품을 찾고 있습니다..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/api/chat",
                    json={"message": prompt},
                    timeout=30
                )
                if response.status_code == 200:
                    reply = response.json()["reply"]
                else:
                    reply = "서버 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
            except requests.exceptions.ConnectionError:
                reply = "백엔드 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인해주세요."
            except Exception as e:
                reply = f"오류가 발생했습니다: {str(e)}"
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

with st.sidebar:
    st.header("💡 사용 팁")
    st.markdown("""
    **이런 질문을 해보세요:**
    - 피부 타입별 추천 (건성/지성/민감성)
    - 가격대별 추천 (1만원 이하, 2만원대)
    - 카테고리별 추천 (스킨케어, 메이크업)
    - 고민별 추천 (여드름, 주름, 미백)
    """)
    
    st.divider()
    
    st.header("🔧 AI 설정 상태")
    aws_region = os.getenv("AWS_REGION", "")
    if aws_region and aws_region != "us-east-1":
        st.success("✅ AWS Bedrock 연동 완료")
    else:
        st.info("ℹ️ Day3에 AWS Bedrock을 연동하세요")
        st.markdown("`.env`에 AWS 인증 정보를 설정해주세요.")
    
    st.divider()
    st.markdown("**사용 기술:** AWS Bedrock (Claude) + DB 데이터")
    
    if st.button("🗑️ 대화 초기화"):
        st.session_state.messages = [
            {"role": "assistant", "content": "대화가 초기화되었습니다. 새로운 질문을 해주세요! 🫒"}
        ]
        st.rerun()
