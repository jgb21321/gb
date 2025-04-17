from authentication import get_input_with_validation  # 이 줄을 꼭 추가하세요

def cloud_security_check():
    print("클라우드 서비스 보안 점검")
    response1 = get_input_with_validation("클라우드 서비스에 중요한 파일을 업로드할 때 암호화를 사용하시나요? (예/아니오): ", ["예", "아니오"])
    response2 = get_input_with_validation("클라우드 계정에 2단계 인증(2FA)을 설정하셨나요? (예/아니오): ", ["예", "아니오"])

    if response1 == "아니오" or response2 == "아니오":
        return "클라우드 서비스의 보안을 강화해야 합니다. 암호화와 2FA 설정을 고려하세요.", 0
    else:
        return "클라우드 보안 설정이 잘 되어 있습니다. 잘 하셨어요!", 1
