from authentication import get_input_with_validation


def privacy_awareness_survey():
    print("개인정보 보호 의식 점검")
    response1 = get_input_with_validation("온라인에서 개인정보를 자주 공유하나요? (예/아니오): ", ["예", "아니오"])
    response2 = get_input_with_validation("개인정보를 저장할 때 안전한 방식으로 저장하나요? (예/아니오): ", ["예", "아니오"])

    if response1 == "예" or response2 == "아니오":
        return "개인정보 보호에 더 신경 써야 합니다.", 0
    else:
        return "개인정보 보호가 잘 이루어지고 있습니다. 계속해서 신경 써주세요!", 1
