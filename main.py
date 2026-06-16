## AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 21005 김보배
# 프로젝트 주제: 사용자 맞춤형 음악 추천 알고리즘 시스템
# 
#  ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 현재 열의 의미:
# 0번 열: 노래 제목
# 1번 열: 가수 (그룹) 이름
# 2번 열: 장르
# 3번 열: '집중하기' 목적 점수
# 4번 열: '분위기띄우기' 목적 점수
# ------------------------------------------------------------
music_db = [
    ['소문의 낙원', 'AKMU(악뮤)', '포크', 90, 30],
    ["Dynamite", "BTS", "댄스", 30, 95],
    ["밤양갱", "비비", "발라드", 70, 30],
    ["Hype Boy", "NewJeans", "댄스", 40, 90],
    ["에피소드", "이무진", "발라드", 85, 40],
    ["시차", "우원재", "힙합", 20, 75],
    ["Super Shy", "NewJeans", "댄스", 45, 95], 
    ["봄날", "BTS", "발라드", 80, 35],    
    ["주저하는 연인들을 위해", "잔나비", "포크", 85, 25],
    ["아로하", "조정석", "발라드", 65, 50],
    ["쉬어", "아넌딜라이트", "힙합", 30, 85],
    ["Love Lee", "AKMU(악뮤)", "포크", 60, 80]
]
# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def calculate_scores(db, user_genre, user_purpose, genre_weight, purpose_weight):
    scored_list = []
    
    for music in db:
        title = music[0]
        artist = music[1]
        genre = music[2]
        study_score = music[3]   
        sports_score = music[4] 
        
        genre_score = 0
        if genre == user_genre:
            genre_score = 100
            
        purpose_score = 0
        if user_purpose == "집중하기":
            purpose_score = study_score
        elif user_purpose == "분위기띄우기":
            purpose_score = sports_score
            

        score = (genre_score * genre_weight) + (purpose_score * purpose_weight)
        
        score = round(score, 1)
        if score > 0:
            scored_list.append([title, artist, score])
        
    return scored_list

def sort_and_print(scored_list):
    scored_list.sort(key=lambda x: x[2], reverse=True)
    
    print("[추천 결과] 딱맞는 음악 TOP 3")
    for i in range(min(3, len(scored_list))):
        print(f"{i+1}위: {scored_list[i][0]} - {scored_list[i][1]} (추천 점수: {scored_list[i][2]}점)")
        
    if len(scored_list) == 0:
        print("조건에 맞는 추천 음악이 없습니다. 입력값을 다르게 하여 다시 시도해 보세요!")

def main():
    print("음악 추천해 드립니다!")
    
    nickname = input("닉네임을 입력하세요: ")
    user_genre = input("선호하는 장르를 입력하세요 (댄스/발라드/힙합/포크): ")
    user_purpose = input("음악을 들으려는 목적을 입력하세요 (집중하기/분위기띄우기): ")
    
    raw_weights = input("장르와 목적의 중요도 백분율을 공백으로 구분해 입력하세요 (예: 60 40): ").split()
    
    genre_weight = int(raw_weights[0]) / 100.0
    purpose_weight = int(raw_weights[1]) / 100.0

    print(f"\n[확인] {nickname}님은 현재 [{user_purpose}] 목적으로 들을 [{user_genre}] 음악을 찾고 계시군요!")
    
    final_scores = calculate_scores(music_db, user_genre, user_purpose, genre_weight, purpose_weight)
    
    sort_and_print(final_scores)



# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------

main()

