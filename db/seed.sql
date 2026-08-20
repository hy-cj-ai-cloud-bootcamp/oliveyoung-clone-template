-- 올리브영 클론 시드 데이터
-- 카테고리 및 상품 초기 데이터

-- 카테고리 데이터
INSERT INTO categories (name, description) VALUES
('스킨케어', '토너, 세럼, 크림 등 기초 스킨케어 제품'),
('메이크업', '파운데이션, 립스틱, 아이섀도 등 색조 화장품'),
('헤어바디', '샴푸, 트리트먼트, 바디워시 등'),
('향수', '오드퍼퓸, 오드뚜왈렛, 바디미스트'),
('건강식품', '비타민, 유산균, 콜라겐 등 건강기능식품'),
('남성', '남성 전용 스킨케어 및 그루밍 제품');

-- 스킨케어 상품 (카테고리 1)
INSERT INTO products (name, brand, price, description, image_url, category_id) VALUES
('히알루론산 수분 토너', '라운드랩', 18000, '히알루론산 성분으로 깊은 수분 공급. 건성, 민감성 피부에 적합한 저자극 토너입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20250718_106%2F1752819122121hXqEF_JPEG%2F6586806071054765_72096548.jpg&type=sc960_832', 1),
('비타C 브라이트닝 세럼', '클레어스', 25000, '순수 비타민C 성분으로 칙칙한 피부톤을 환하게 개선해줍니다. 모든 피부 타입 사용 가능.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA1MTJfMTg0%2FMDAxNzE1NTA3OTE0NzUw.0tTJgfgNen5Z6MJBJb1HJyWFDVuZ9JZvylQCPVKeHUog.cSjB9BUd7z3_EXnpimKByIMg6uzC3_ZD838yrcYHP7sg.PNG%2Fimage.png&type=sc960_832', 1),
('세라마이드 수분크림', '이니스프리', 22000, '세라마이드 성분이 피부 장벽을 강화하고 수분을 오래 유지시켜줍니다. 건성 피부 추천.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_1341132%2F13411322875.9.jpg&type=f372_372', 1),
('녹차 시드 에센스', '이니스프리', 32000, '제주 녹차 씨앗 성분으로 피부에 생기를 불어넣는 고농축 에센스입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTEyMTJfMTA3%2FMDAxNzY1NTE2Mjg2Nzc3.liohXh11_d_iIgMRsBJ_DdeTwfRv3EFb6TQSA-eButMg.Q6rYNOZ6GzbvE33_Di20ZX-fdkSVEV6Y865Y69vMy7Ig.PNG%2Fimage.png&type=a340', 1),
('티트리 진정 앰플', '메디힐', 15000, '트러블 피부를 빠르게 진정시키는 티트리 성분 앰플. 지성, 여드름 피부 추천.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fimage.nmv.naver.net%2Fblog_2025_10_22_748%2F0Ae6x76dOm_01.jpg&type=a340', 1),
('레티놀 인텐스 크림', '토리든', 28000, '레티놀 성분으로 주름 개선과 피부 탄력에 도움을 주는 안티에이징 크림입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20260225_108%2F1771980908239QsvYL_JPEG%2F106113700305580969_770238172.jpg&type=a340', 1),
('판테놀 시카 밤', '라운드랩', 16000, '판테놀과 시카 성분으로 손상된 피부를 회복시켜주는 진정 밤입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20250725_68%2F1753381782607DmtkP_JPEG%2F19567610050844346_183603556.jpg&type=a340', 1),
('콜라겐 아이크림', '에스트라', 35000, '눈가 주름과 다크서클을 개선하는 콜라겐 성분의 아이크림입니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8690819%2F86908199256.2.jpg&type=f372_372', 1),
('알로에 수딩 젤', '네이처리퍼블릭', 8000, '92% 알로에 성분으로 자극받은 피부를 즉각 진정시키는 수딩 젤입니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_9113121%2F91131217711.jpg&type=f372_372', 1),
('AHA BHA 클렌징 폼', '코스알엑스', 12000, '약산성 AHA/BHA 성분으로 모공 속 노폐물을 제거하는 클렌징 폼입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMTBfMTY1%2FMDAxNzI4NTQyODc3NDc1.cIr5iwYfuq3Vz60qBsYQ73BOUWjvyoZgXPQD-_Iduoog.XwF0MK2Ok7Gwu7SrQkesIMOxDyKrhiV5dBKCAjK5vLUg.JPEG%2FKakaoTalk_20241010_152217716_03.jpg&type=a340', 1);

-- 메이크업 상품 (카테고리 2)
INSERT INTO products (name, brand, price, description, image_url, category_id) VALUES
('벨벳 립 틴트 로즈', '롬앤', 12000, '부드러운 벨벳 텍스처의 로즈 컬러 립 틴트. 지속력이 뛰어나고 각질 부각이 없습니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDAzMTBfNjEg%2FMDAxNTgzODM4Nzg4Nzg3.087v4cxNHFYjEKNAZnNjpZqwxuTzVyCG8zRj10vGaV8g.QVXDADrgAE-xokpE1FG_NAZttSSoFywa6-5gyAMWZNIg.JPEG.euimok%2FDSC05317.jpg&type=a340', 2),
('글로우 쿠션 파운데이션', '클리오', 28000, '자연스러운 광채 피부를 연출하는 쿠션 파운데이션. SPF50+ PA+++ 자외선 차단 기능.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20210716_66%2F16263964198831PflL_JPEG%2F27532265599698405_183702588.jpg&type=a340', 2),
('멀티 아이팔레트 12색', '에뛰드', 25000, '데일리부터 파티룩까지 다양한 12가지 컬러의 아이섀도 팔레트입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNjA3MDdfMjYy%2FMDAxNzgzMzc5MzE3NTAz.wqMRm-95KjhaJVlCioZEJUxzeD2a00urqmcKaEbpjhgg.r8AwsM3VrZab6ocNgAfVIFAKa_rMSuzQTC7gqM4IDfog.JPEG%2Fphoto_20260707_080711_605_raw.jpg&type=a340', 2),
('워터프루프 마스카라', '헤라', 22000, '번짐 없이 하루종일 유지되는 워터프루프 마스카라. 볼륨과 컬링 동시에.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20251024_107%2F1761303474945L4yGe_JPEG%2F9279467958022648_2000736230.jpg&type=a340', 2),
('파우더 블러셔 피치', '이니스프리', 15000, '자연스러운 피치 컬러 블러셔. 미세한 입자로 부드럽게 발립니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F030%2F2016%2F02%2F17%2Farticle_17180335819365_99_20160217183019.jpg&type=a340', 2),
('프로 컨실러', '더샘', 8000, '강력한 커버력의 리퀴드 컨실러. 다크서클과 잡티를 자연스럽게 커버합니다.', 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fimage.msscdn.net%2Fthumbnails%2Fimages%2Fprd_img%2F20230622%2F3378154%2Fdetail_3378154_16874121763787_500.jpg&type=a340', 2),
('매트 립스틱 레드', '맥', 35000, '클래식 레드 컬러의 매트 립스틱. 풍부한 발색과 긴 지속력이 특징입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20181130_297%2Fbeautylab_1543540457521AjzCj_JPEG%2F8eb5c4f4035c4289cfa95ecc000efd7e.jpg&type=a340', 2),
('글리터 아이라이너', '클리오', 16000, '파티룩에 딱 어울리는 글리터 아이라이너. 쉽게 번지지 않습니다.', 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fimage.msscdn.net%2Fimages%2Fgift_img%2F2023050209421200000036648.jpg&type=a340', 2);

-- 헤어바디 상품 (카테고리 3)
INSERT INTO products (name, brand, price, description, image_url, category_id) VALUES
('다마스크 로즈 샴푸', '아모스', 18000, '다마스크 로즈 오일이 함유된 고보습 샴푸. 건조하고 손상된 모발에 영양을 공급합니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20210202_202%2F1612239656432orIR1_JPEG%2F13375554872852525_1487027470.jpg&type=a340', 3),
('케라틴 헤어 트리트먼트', '미장센', 14000, '케라틴 성분으로 손상된 모발을 복구하는 트리트먼트. 염색/펌 후 케어에 적합.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTEwMDVfMjUz%2FMDAxNzU5NjQyNTU2MjM5.TGylmqTjRF05KZwQFwEXe-T-ohPTU50jowH_ISwfRWUg.hFZR_eI0juECl0Ja27qtU-lyy0KnlPgv1KN-g8TRpIIg.JPEG%2Fimage.jpg&type=a340', 3),
('시어버터 바디로션', '존슨즈', 12000, '시어버터 성분으로 건조한 피부에 깊은 보습을 제공하는 바디로션입니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_5838392%2F58383923135.jpg&type=f372_372', 3),
('프레시 바디워시 자몽', '해피바스', 9000, '상큼한 자몽 향으로 기분 좋은 샤워 시간을 만들어주는 바디워시입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20211023_112%2F1634959954384goMQ9_JPEG%2F3725592bfa8798e298d2.jpg&type=a340', 3),
('두피 스케일링 토닉', '닥터포헤어', 25000, '두피 각질과 유분을 제거하는 스케일링 토닉. 건강한 두피 환경을 만듭니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMjFfMjcx%2FMDAxNTc0MzIwMzY1NjU5.psbF9MG8EElMvP732LQoFOTswN4YHmCxqiQB78V7u80g.H-MU1pzcVnkewpACnRVq_W9LcD0y8LpPTMvXOsXSgm8g.PNG.nahb0%2F11.PNG&type=a340', 3),
('헤어 에센스 오일', '모로칸오일', 38000, '아르간 오일이 함유된 헤어 에센스. 푸석한 모발에 윤기를 더합니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20201207_32%2F1607319571369qss8w_JPEG%2F8455406205237176_471168009.jpg&type=a340', 3);

-- 향수 상품 (카테고리 4)
INSERT INTO products (name, brand, price, description, image_url, category_id) VALUES
('화이트 머스크 퍼퓸', '딥디크', 45000, '깨끗하고 포근한 화이트 머스크 향. 은은하게 지속되는 고급스러운 향수입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzExMDFfMjQx%2FMDAxNjk4NzcxMDI5NTI2.Ql-U_8nozdJGfPG7ZFBVHAvAQ1aGwC1UlP2l_5HYdxEg.Jz9i3OARTqf2J_gzsVvNM7MHC88Wb93_D6-fuITga6Ag.PNG.gomzi_modak%2F9.png&type=a340', 4),
('로즈 가든 오드퍼퓸', '조말론', 55000, '영국식 정원의 장미향을 담은 오드퍼퓸. 우아하고 여성스러운 향입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20221020_85%2F1666250512731Sqmzx_JPEG%2F67386358440012482_1100112588.jpg&type=a340', 4),
('시트러스 바디미스트', '빅토리아시크릿', 22000, '상큼한 시트러스 향의 바디미스트. 가볍게 뿌리기 좋은 데일리 향수입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshopping.phinf.naver.net%2Fmain_5938882%2F59388827737.20260325175910.jpg&type=a340', 4),
('우디 오드뚜왈렛', '이솝', 65000, '깊고 차분한 우드 계열 향. 남녀 공용으로 사용 가능한 유니섹스 향수입니다.', 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fthumbnail.coupangcdn.com%2Fthumbnails%2Fremote%2F492x492ex%2Fimage%2Fvendor_inventory%2Fbc48%2Ffd09d10fae4240ddffe3a5a7a1d453075bb8da2b8655d5eca6b1e4f76dc1.png&type=a340', 4);

-- 건강식품 상품 (카테고리 5)
INSERT INTO products (name, brand, price, description, image_url, category_id) VALUES
('멀티비타민 30일분', '센트룸', 28000, '하루 한 알로 필수 비타민과 미네랄을 섭취할 수 있는 종합비타민입니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshop-phinf.pstatic.net%2F20230621_289%2F1687320594461BuO86_PNG%2F485869436251942_1141207718.png&type=a340', 5),
('프로바이오틱스 유산균', '종근당', 32000, '장 건강에 도움을 주는 100억 CFU 프로바이오틱스 유산균입니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8597450%2F85974505609.11.jpg&type=f372_372', 5),
('저분자 피쉬 콜라겐', '에버콜라겐', 35000, '흡수율 높은 저분자 피쉬 콜라겐. 피부 탄력과 수분 유지에 도움을 줍니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8877280%2F88772800296.1.jpg&type=f372_372', 5),
('루테인 눈건강', '안국건강', 25000, '눈의 피로를 줄이고 황반 건강에 도움을 주는 루테인 영양제입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA3MjdfMjA0%2FMDAxNjI3MzYxNTM3NTM2.aAikdftIQ8jHxd8sO-EykAjQQ_g6olipPp7cullFIm8g.HcG_H0pHMgeXFBViwEJxs9apPKeLQiCDAhVwwWyl1b0g.JPEG.dhlrn294%2F8d95105be0b8d8b.jpg&type=a340', 5),
('비타민C 1000mg', '고려은단', 15000, '면역력 증진과 피부 건강에 도움을 주는 고함량 비타민C입니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshop-phinf.pstatic.net%2F20260119_62%2F1768820965460DXz8Q_JPEG%2F21535277581474617_68765776.jpg&type=a340', 5);

-- 남성 상품 (카테고리 6)
INSERT INTO products (name, brand, price, description, image_url, category_id) VALUES
('올인원 스킨로션', '비오템 옴므', 35000, '세안 후 하나로 끝내는 남성용 올인원 스킨로션. 간편한 데일리 케어.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_7434871%2F7434871275.22.jpg&type=f372_372', 6),
('쿨링 셰이빙 폼', '니베아맨', 8000, '쿨링 성분으로 면도 시 자극을 최소화하는 셰이빙 폼입니다.', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNjA0MTFfNzkg%2FMDAxNzc1ODc3ODE5Nzkw.BiSsR4Rxs1KnJwf5QYqI9fZIM6PQC98ntlk5N8Cu758g.ZDqAJ9QgCNIKfA9zDvgE7KUpBGisBSpz3F_CUsqWDNgg.JPEG%2Fprocessed_1.jpg&type=a340', 6),
('남성용 선크림 SPF50', '라네즈 옴므', 25000, '끈적임 없는 산뜻한 사용감의 남성용 선크림. 자외선 차단 SPF50+ PA+++', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20260303_224%2F1772524717747rinRT_JPEG%2F2525170854565380_1539700475.jpg&type=a340', 6),
('헤어왁스 매트', '갸스비', 9000, '자연스러운 매트 텍스처의 헤어왁스. 강력한 홀드력으로 스타일 유지.', 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fcdn2.halfclub.com%2Fcdn%2Fproduct%2FSA002582%2FP326883727%2F1_P326883727_basic_1738250695238.jpg&type=a340', 6),
('두피 클렌징 샴푸', '닥터포헤어', 18000, '남성 두피 유분과 비듬을 효과적으로 제거하는 클렌징 샴푸입니다.', 'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_9107204%2F91072041168.jpg&type=f372_372', 6);
