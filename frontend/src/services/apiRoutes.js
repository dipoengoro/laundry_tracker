export const apiRoutes = {
    // Autentikasi
    LOGIN: '/token/',
    REGISTER: '/users/register/',
    USER_DETAIL: '/users/me/',
    REFRESH_TOKEN: '/token/refresh/',

    // Katalog
    CLOTHING_ITEMS: '/catalog/items/',
    CLOTHING_ITEM_DETAIL: (id) => `/catalog/items/${id}/`
}