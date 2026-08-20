"""
환경변수 설정 모듈
.env 파일 또는 환경변수에서 설정값을 읽어옵니다.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# 데이터베이스 설정
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://oliveyoung:oliveyoung123@db:5432/oliveyoung")

# JWT 설정
JWT_SECRET = os.getenv("JWT_SECRET", "your-jwt-secret-key-here")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

# AWS Bedrock 설정 (Day3에 사용)
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0")
