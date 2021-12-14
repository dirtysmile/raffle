from selenium import webdriver
import time
import datetime

import send_telegram
import crawling_info


err_cnt = 0
instar_nike_pages = [{'title': '할라피뇨맨', 'url': 'https://www.instagram.com/dirtysmile89/', 'is_docs': True},
                     {'title': '나이키 홍대',
                         'url': 'https://www.instagram.com/nike_hongdae/', 'is_docs': True},
                     {'title': '나이키 서현',
                         'url': 'https://www.instagram.com/nike__seohyeon/', 'is_docs': True},
                     {'title': '나이키 신촌',
                         'url': 'https://www.instagram.com/nike_sinchon/', 'is_docs': True},
                     {'title': '나이키 디큐브',
                         'url': 'https://www.instagram.com/nike_dcubecity/', 'is_docs': True},
                     {'title': '나이키 영등포롯데',
                      'url': 'https://www.instagram.com/nike_lotteyeongdeungpo/', 'is_docs': True},
                     {'title': '나이키 메세나 합정',
                      'url': 'https://www.instagram.com/nike_mecena_hapjeong/', 'is_docs': True},
                     {'title': '나이키 신림',
                         'url': 'https://www.instagram.com/nike_sillim/', 'is_docs': True},
                     {'title': '나이키 명동', 'url': 'https://www.instagram.com/nike_myeongdong_official/', 'is_docs': True},
                     {'title': '나이키 문정', 'url': 'https://www.instagram.com/nike_munjeong_official/', 'is_docs': True},
                     {'title': '나이키 롯데광주',
                      'url': 'https://www.instagram.com/nike__lottegwangju/', 'is_docs': True},
                     {'title': '나이키 타임스퀘어',
                      'url': 'https://www.instagram.com/nike_timessquare/', 'is_docs': True},
                     {'title': '나이키 수원 AK',
                      'url': 'https://www.instagram.com/_ak_suwon_nike/', 'is_docs': True},
                     {'title': '나이키 코엑스',
                         'url': 'https://www.instagram.com/coex_nike_/', 'is_docs': True},
                     {'title': '나이키 롯데 인천터미널',
                      'url': 'https://www.instagram.com/lotte_incheon_nike_/', 'is_docs': True},
                     {'title': '나이키 용산 아이파크',
                      'url': 'https://www.instagram.com/ipark_yongsan_nike/', 'is_docs': True},
                     {'title': '나이키 이태원 타운',
                      'url': 'https://www.instagram.com/nikesports_itaewontown/', 'is_docs': True},
                     {'title': '나이키 강남',
                         'url': 'https://www.instagram.com/nike_gangnam/', 'is_docs': True},
                     {'title': '나이키 압구정',
                         'url': 'https://www.instagram.com/nike_apgujeong/', 'is_docs': True},
                     {'title': '나이키 잠실',
                         'url': 'https://www.instagram.com/nike_jamsil/', 'is_docs': True},
                     {'title': '나이키 롯데분당',
                      'url': 'https://www.instagram.com/nike_lottebundang/', 'is_docs': True},
                     {'title': '나이키 더현대 서울',
                      'url': 'https://www.instagram.com/nike_thehyundaiseoul/', 'is_docs': True},
                     {'title': '나이키 롯데 광주',
                      'url': 'https://www.instagram.com/nike__lottegwangju/', 'is_docs': True},
                     {'title': '나이키 롯데 김포스카이파크',
                      'url': 'https://www.instagram.com/nike_gimposkypark/', 'is_docs': True},
                     {'title': '나이키 의왕',
                         'url': 'https://www.instagram.com/nike_uiwang/', 'is_docs': True},
                     {'title': '나이키 현대 충정점',
                      'url': 'https://www.instagram.com/nike_chungcheong/', 'is_docs': True},
                     {'title': '나이키 두타',
                         'url': 'https://www.instagram.com/doota_nike/', 'is_docs': True},
                     {'title': '나이키 광명',
                         'url': 'https://www.instagram.com/nike_gwangmyeong/', 'is_docs': True},
                     {'title': '나이키 롯데 동래',
                      'url': 'https://www.instagram.com/lottedongnae_nike/', 'is_docs': True},
                     {'title': '나이키 송파',
                         'url': 'https://www.instagram.com/nike_songpa/', 'is_docs': True},
                     {'title': '나이키 강남 플래그쉽 스토어',
                      'url': 'https://www.instagram.com/nike_gangnam/', 'is_docs': True},
                     {'title': '나이키 동성로타운',
                      'url': 'https://www.instagram.com/nike_dongseongrotown/', 'is_docs': True},
                     {'title': '나이키 월드몰',
                         'url': 'https://www.instagram.com/nike_worldmall/', 'is_docs': True},
                     {'title': '나이키 간석',
                         'url': 'https://www.instagram.com/nike_ganseok/', 'is_docs': True},
                     {'title': '나이키 노량진',
                         'url': 'https://www.instagram.com/nrj_nike/', 'is_docs': True},
                     {'title': '나이키 올림픽',
                         'url': 'https://www.instagram.com/olympic.nike/', 'is_docs': True},
                     {'title': '나이키 신세계 대구',
                      'url': 'https://www.instagram.com/nike_ssg_daegu/', 'is_docs': True},
                     {'title': '나이키 부평',
                         'url': 'https://www.instagram.com/nike_bupyeong/', 'is_docs': True},
                     {'title': '나이키 롯데몰 수지',
                      'url': 'https://www.instagram.com/nike_sujimall/', 'is_docs': True},
                     {'title': '나이키 원주타운',
                         'url': 'https://www.instagram.com/nike_wonju_town/', 'is_docs': True},
                     {'title': '나이키 롯데 일산',
                         'url': 'https://www.instagram.com/ilsan_dsnike/', 'is_docs': True},
                     {'title': '나이키 엔터식스 안양',
                      'url': 'https://www.instagram.com/nike_enter6_anyang/', 'is_docs': True},
                     {'title': '나이키 현대 목동',
                      'url': 'https://www.instagram.com/nike_hyundai_mokdong/', 'is_docs': True},
                     {'title': '나이키 엔터식스 왕십리',
                      'url': 'https://www.instagram.com/enter6_wangsimni_nike/', 'is_docs': True},
                     {'title': '나이키 동탄',
                         'url': 'https://www.instagram.com/nike_dongtan/', 'is_docs': True},
                     {'title': '나이키 현대 신촌',
                         'url': 'https://www.instagram.com/nike_sinchon/', 'is_docs': True},
                     {'title': '나이키 현대 중동',
                         'url': 'https://www.instagram.com/nike_jungdong/', 'is_docs': True},
                     {'title': '나이키 신세계 아트앤사이언스 대전',
                      'url': 'https://www.instagram.com/nike_ssg_daejeon/', 'is_docs': True},
                     {'title': '나이키 신세계 의정부',
                      'url': 'https://www.instagram.com/nike_ssg_uijeongbu/', 'is_docs': True},
                     {'title': '나이키 AK 평택',
                      'url': 'https://www.instagram.com/ak_pyeongtaek_nike/', 'is_docs': True},
                     {'title': '나이키 롯데 수원',
                      'url': 'https://www.instagram.com/lotte_suwon_nike/', 'is_docs': True},
                     {'title': '나이키 금촌',
                         'url': 'https://www.instagram.com/geumchon_nike/', 'is_docs': True},
                     {'title': '나이키 서면',
                         'url': 'https://www.instagram.com/shoeland_bb/', 'is_docs': True}
                     ]

previous_histories = []
recent_histories = []


def login(driver):
    login_url = "https://www.instagram.com/accounts/login/"
    driver.get(login_url)

    user_id = crawling_info.get_user_id()
    user_passwd = crawling_info.get_user_passwd()
    instagram_id_name = 'username'
    instagram_pw_name = 'password'
    instagram_login_btn = '#loginForm > div > div:nth-child(3)'

    time.sleep(2)

    # 아이디 입력
    instagram_id_form = driver.find_element_by_name(instagram_id_name)
    instagram_id_form.send_keys(user_id)

    # 비밀번호 입력
    instagram_pw_form = driver.find_element_by_name(instagram_pw_name)
    instagram_pw_form.send_keys(user_passwd)

    # 로그인 버튼
    login_ok_button = driver.find_element_by_css_selector(instagram_login_btn)
    login_ok_button.click()

    time.sleep(10)

    if driver.current_url == login_url:
        print('로그인 실패 30분후 재시도')
        time.sleep(1800)
        login(driver)
    else:
        print('로그인 성공')

    return driver


def get_docs(driver, url):
    # 페이지 이동
    driver.get(url)

    time.sleep(7)
    title = ""
    docs_url = ""
    links = []
    global err_cnt

    try:
        title = driver.find_element_by_tag_name('h1')
        title = title.text
        docs_url = ""

        links = driver.find_elements_by_xpath("//a[@href]")

        if len(links) > 0:
            for link in links:
                link_href = link.get_attribute("href")
                if link_href.find('docs.google.com') > 0:
                    docs_url = link_href.split('=')[1].replace(
                        "%2F", "/").replace("%3A", ":").split("%3")[0]

            return title, docs_url
        else:
            return False
    except Exception as e:
        err_cnt = err_cnt+1
        return False


def run(driver, instar_nike_pages, recent_histories, previous_histories):
    global err_cnt
    now = datetime.datetime.now()
    print(now)

    for link in instar_nike_pages:
        docs = get_docs(driver, link['url'])
        print(docs)

        if docs != False and docs[1] != '':
            if docs[1] not in previous_histories:
                previous_histories.append(docs[1])
                recent_histories.append({'title': docs[0], 'url': docs[1]})

    if err_cnt > 0:
        send_telegram.send_error('크롤링 실패')
        err_cnt = 0

    if len(recent_histories) > 0:
        send_telegram.send_telgm(recent_histories)
