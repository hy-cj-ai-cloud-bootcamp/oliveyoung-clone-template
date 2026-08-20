/**
 * 올리브영 클론 - 프론트엔드 공통 JavaScript
 * 
 * 백엔드 API와 통신하는 유틸리티 함수 모음
 * fetch API를 사용하여 REST API를 호출합니다.
 */

// API 기본 URL (Nginx 프록시를 통해 /api로 접근)
const API_BASE = '/api';

// ===== API 통신 유틸리티 =====
const api = {
    // GET 요청
    async get(url) {
        const response = await fetch(url, {
            headers: getAuthHeaders()
        });
        if (!response.ok) throw await response.json();
        return response.json();
    },

    // POST 요청
    async post(url, data) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...getAuthHeaders()
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw await response.json();
        return response.json();
    },

    // PUT 요청
    async put(url, data) {
        const response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                ...getAuthHeaders()
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw await response.json();
        return response.json();
    },

    // DELETE 요청
    async delete(url) {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: getAuthHeaders()
        });
        if (!response.ok) throw await response.json();
        return response.json();
    }
};

// ===== 인증 관련 =====

// JWT 토큰을 헤더에 포함
function getAuthHeaders() {
    const token = localStorage.getItem('token');
    if (token) {
        return { 'Authorization': `Bearer ${token}` };
    }
    return {};
}

// 로그인 상태 확인 및 UI 업데이트
function checkAuth() {
    const token = localStorage.getItem('token');
    const username = localStorage.getItem('username');
    const authButtons = document.getElementById('auth-buttons');
    const userMenu = document.getElementById('user-menu');
    const userName = document.getElementById('user-name');

    if (token && authButtons && userMenu) {
        authButtons.style.display = 'none';
        userMenu.style.display = 'flex';
        if (userName) userName.textContent = `${username}님`;
    }
}

// 로그아웃
function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    window.location.href = '/';
}

// 로그인 필요 페이지 체크
function requireAuth() {
    const token = localStorage.getItem('token');
    if (!token) {
        alert('로그인이 필요합니다.');
        window.location.href = '/pages/login.html';
        return false;
    }
    return true;
}

// ===== 장바구니 관련 =====

// 장바구니에 상품 추가
async function addToCart(productId, quantity = 1) {
    if (!requireAuth()) return;
    try {
        await api.post('/api/cart', { product_id: productId, quantity });
        alert('장바구니에 추가되었습니다!');
        updateCartCount();
    } catch (e) {
        alert(e.detail || '장바구니 추가 실패');
    }
}

// 장바구니 수량 업데이트
async function updateCartCount() {
    try {
        const items = await api.get('/api/cart');
        const countEl = document.getElementById('cart-count');
        if (countEl) {
            const total = items.reduce((sum, item) => sum + item.quantity, 0);
            countEl.textContent = total;
        }
    } catch (e) {
        // 로그인 안 된 경우 무시
    }
}

// ===== 유틸리티 =====

// URL 쿼리 파라미터 가져오기
function getQueryParam(key) {
    const params = new URLSearchParams(window.location.search);
    return params.get(key);
}

// 가격 포맷팅
function formatPrice(price) {
    return Number(price).toLocaleString() + '원';
}

// 메시지 표시
function showMessage(container, message, type = 'success') {
    const el = document.createElement('div');
    el.className = `message message-${type}`;
    el.textContent = message;
    container.prepend(el);
    setTimeout(() => el.remove(), 3000);
}

// 페이지 로드 시 장바구니 카운트 업데이트
document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
});
