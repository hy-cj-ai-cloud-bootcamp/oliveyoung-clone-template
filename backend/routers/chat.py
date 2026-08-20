"""
AI 챗봇 라우터 (스켈레톤)

[Day3 구현 가이드]
이 파일은 AI 챗봇 API 엔드포인트입니다.
학생들이 Day3에 AWS Bedrock을 연동하여 완성합니다.

구현 방식:
- DB에서 상품 데이터를 조회하여 프롬프트 컨텍스트로 사용
- AWS Bedrock의 FM(Claude)에 상품 정보 + 사용자 질문을 전달
- AI가 상품 데이터 기반으로 추천 답변 생성

사전 준비:
- AWS CLI 설정 (aws configure)
- Bedrock 모델 접근 권한 활성화 (Claude 3 Sonnet 등)
- .env에 AWS_REGION, BEDROCK_MODEL_ID 설정
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import ChatRequest, ChatResponse
from crud import get_all_products_for_chat
from config import AWS_REGION, BEDROCK_MODEL_ID

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """
    AI 챗봇 엔드포인트 (AWS Bedrock)
    
    사용 예시:
    - "건성 피부에 좋은 제품 추천해줘"
    - "1만원 이하 립스틱 보여줘"
    - "수분크림 추천해줘"
    
    [TODO] Day3에 아래 내용을 구현하세요:
    1. DB에서 상품 정보 조회 (이미 구현됨)
    2. 상품 정보를 프롬프트에 포함
    3. Bedrock InvokeModel API 호출
    4. 응답 반환
    """
    user_message = request.message
    
    # [Step 1] DB에서 상품 정보 가져오기 (컨텍스트로 사용)
    products = get_all_products_for_chat(db)
    product_info = "\n".join([
        f"- {p.name} (브랜드: {p.brand}, 가격: {p.price}원, 카테고리ID: {p.category_id}) - {p.description}"
        for p in products
    ])
    
    # ============================================
    # TODO: 여기에 AWS Bedrock 연동 코드를 작성하세요
    # ============================================
    """
    import boto3
    import json
    
    # Bedrock Runtime 클라이언트 생성
    client = boto3.client('bedrock-runtime', region_name=AWS_REGION)
    
    # 프롬프트 구성 - DB의 상품 데이터를 컨텍스트로 포함
    prompt = f'''당신은 올리브영의 뷰티 제품 추천 전문가입니다.
아래 상품 목록을 참고하여 고객의 질문에 친절하게 답변해주세요.
상품 추천 시 가격과 특징을 함께 안내해주세요.

[보유 상품 목록]
{product_info}

[고객 질문]
{user_message}

친절하고 전문적인 톤으로 한국어로 답변해주세요.'''
    
    # Claude 모델 호출
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    })
    
    response = client.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        body=body,
        contentType='application/json'
    )
    
    result = json.loads(response['body'].read())
    reply = result['content'][0]['text']
    return ChatResponse(reply=reply)
    """
    
    # [임시 응답] Bedrock 연동 전까지 사용되는 더미 응답
    return ChatResponse(
        reply=f"[AI 챗봇 준비 중] '{user_message}'에 대한 답변을 준비하고 있습니다. "
              f"Day3에 AWS Bedrock을 연동하면 실제 AI 추천을 받을 수 있습니다! "
              f"현재 DB에 {len(products)}개의 상품이 등록되어 있습니다."
    )
