const cart = document.querySelector('.cart');

const swiper = new Swiper('.slider', {
    direction: 'vertical',
    allowTouchMove: false,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    mousewheel: true,
});
const mobileSwiper = new Swiper('.mobile-slider__container', {
    mousewheel: false,
    pagination: {
        el: '.mobile-slider__pagination',
        clickable: true,
    },
    loop: true,
    navigation: {
        prevEl: '.mobile-slider__navigation_prev',
        nextEl: '.mobile-slider__navigation_next'
    },
    mousewheel: false,
});

function cartOpenClose(selector) {

    if (!cart) return;

    const button = cart.querySelector('.cart__button');
    const closeButtons = cart.querySelectorAll('.cart__close');
    button.addEventListener('click', (e) => {
        if (!document.querySelector('.cart__overlay')) {
            const overlay = document.createElement('div');
            overlay.classList.add('cart__overlay');
            document.body.appendChild(overlay);
            overlay.addEventListener('click', hideCart);
        }

        cart.classList.add('cart__open');
    });
    closeButtons.forEach((btn) => {
        btn.addEventListener('click', hideCart);
    });


}

cartOpenClose();

function hideCart() {
    cart.classList.remove('cart__open');
    const overlay = document.querySelector('.cart__overlay');
    if (overlay) overlay.remove();
}


function customRadioButtons(productClass) {

    const products = document.querySelectorAll(productClass);
    products.forEach(product => {
        const buttons = product.querySelectorAll('.product__sizes label')
        buttons.forEach((btn) => {
            btn.addEventListener('click', (e) => {
                const priceButtons = product.querySelectorAll(`.${e.target.dataset.button}`)
                priceButtons.forEach(b => b.classList.remove('product__price-active'))
                const priceButton = product.querySelector(`.product__price-${e.target.id}`)
                if (priceButton) priceButton.classList.add('product__price-active');

                buttons.forEach((btn) =>
                    btn.classList.remove('product__size_active')
                );
                console.log(buttons)

                btn.classList.add('product__size_active');
            });
        });
    })

}

customRadioButtons('.product');

function countInputs(selector) {
    const selectors = document.querySelectorAll(selector);
    selectors.forEach((item) => {
        const buttons = item.querySelectorAll('button');
        const input = item.querySelector('input');
        buttons[0].addEventListener('click', () => {
            if (+input.value > 1) {
                input.value = +input.value - 1;
            }
        });
        buttons[1].addEventListener(
            'click',
            () => (input.value = +input.value + 1)
        );
        input.addEventListener('change', () => {
            if (input.value < 1) {
                input.value = 1;
            }
        });
    });
}

countInputs('.product__count');

function dropDown(selector) {
    const items = document.querySelectorAll(selector);
    items.forEach((item, i) => {
        const btn = item.querySelector('.dropdown__title');
        btn.dataset.id = i;
        btn.dataset.dropdown = 1;
        const content = item.querySelector('.dropdown__content');
        btn.addEventListener('click', () => {
            const contents = document.querySelectorAll('.dropdown__content');
            const buttons = document.querySelectorAll('.dropdown__title');
            contents.forEach((c, i) => {
                if (i != btn.dataset.id) {
                    c.classList.remove('dropdown__content-active');
                    buttons[i].classList.remove('dropdown__title-active');
                }
            });
            btn.classList.toggle('dropdown__title-active');
            content.classList.toggle('dropdown__content-active');
            document.addEventListener('click', (e) => {
                if (!e.target.dataset.dropdown) {
                    contents.forEach((c, i) => {
                        c.classList.remove('dropdown__content-active');
                        buttons[i].classList.remove('dropdown__title-active');
                    });
                }
            })
        });
    });
}

dropDown('.dropdown');

function openMobileMenu() {
    const burger = document.querySelector('.mobile-header__burger');
    if (!burger) return;
    burger.addEventListener('click', () => {
        const menu = document.querySelector('.mobile-header__menu_items');
        const close = menu.querySelector('.mobile-header__menu_items-close');
        burger.style.display = 'none'
        menu.classList.add('mobile-header__menu_items-active');
        close.addEventListener('click', () => {
            menu.classList.remove('mobile-header__menu_items-active');
            burger.style.display = 'flex'
        })
    })
}

openMobileMenu()


function mobileProductDropdown() {
    const products = document.querySelectorAll('.mobile__product');
    if (!products.length) return;
    products.forEach(product => {
        const title = product.querySelector('.mobile__product_title');
        title.addEventListener('click', (e) => {
            const info = product.querySelector('.mobile__product_info')
            title.classList.toggle('mobile__product_title-opened')
            info.classList.toggle('mobile__product_info-opened')
        })
    })
}

mobileProductDropdown()


// const API_URL = 'https://grtak.am';

const API_URL = 'http://127.0.0.1:8000';

async function getCartItems(url) {
    const data = await fetch(url);
    const res = await data.json();

    return res
}

async function cleanCart() {
    const data = await fetch(`${API_URL}/cart/clean`);
    return await data.json();

}

getCartItems(`${API_URL}/cart`)
    .then(data => {
        renderProductInCheckoutPage(data)
        cartRender(data)
    })

function cartRender(data) {
    if (!cart) return;
    const productContainer = cart.querySelector('.cart__content_products')
    const totalPrice = cart.querySelector('.cart__sum')
    const cartFooter = cart.querySelector('.cart__content_footer')
    productContainer.innerHTML = '';
    if (!Object.keys(data.cart).length) {
        cart.classList.add('cart__empty');
        hideCart()
        return;
    } else {
        cart.classList.remove('cart__empty');
    }
    Object.values(data.cart).map(item => {
        const html = `
        <li class="cart__content_product">
                        <img src="${item.product.mobile_img}" alt="${item.product.name}"/>
                        <div class="cart__content_product-info">
                            <h3 class="cart__content_product-info-name">${item.product.name}</h3>
                            <div class="cart__content_product-info-row">
                                <p class="cart__content_product-info-size">${item.size} SM</p>
                                <input  type="number" value="${item.quantity}" data-size="${item.size}" data-product-id="${item.product.id}" class="cart__item_quantity" />
                            </div>
                            <p class="cart__content_product-info-price">${item.price} AMD</p>
                        </div>
                        <button class="cart__content_product-trash" data-product-id="${item.product.id}" data-product-size="${item.size}">
                            <svg
                                    width="16"
                                    height="16"
                                    viewBox="0 0 16 16"
                                    fill="none"
                                    xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                        d="M5.5 5.5C5.63261 5.5 5.75979 5.55268 5.85355 5.64645C5.94732 5.74021 6 5.86739 6 6V12C6 12.1326 5.94732 12.2598 5.85355 12.3536C5.75979 12.4473 5.63261 12.5 5.5 12.5C5.36739 12.5 5.24021 12.4473 5.14645 12.3536C5.05268 12.2598 5 12.1326 5 12V6C5 5.86739 5.05268 5.74021 5.14645 5.64645C5.24021 5.55268 5.36739 5.5 5.5 5.5ZM8 5.5C8.13261 5.5 8.25979 5.55268 8.35355 5.64645C8.44732 5.74021 8.5 5.86739 8.5 6V12C8.5 12.1326 8.44732 12.2598 8.35355 12.3536C8.25979 12.4473 8.13261 12.5 8 12.5C7.86739 12.5 7.74021 12.4473 7.64645 12.3536C7.55268 12.2598 7.5 12.1326 7.5 12V6C7.5 5.86739 7.55268 5.74021 7.64645 5.64645C7.74021 5.55268 7.86739 5.5 8 5.5ZM11 6C11 5.86739 10.9473 5.74021 10.8536 5.64645C10.7598 5.55268 10.6326 5.5 10.5 5.5C10.3674 5.5 10.2402 5.55268 10.1464 5.64645C10.0527 5.74021 10 5.86739 10 6V12C10 12.1326 10.0527 12.2598 10.1464 12.3536C10.2402 12.4473 10.3674 12.5 10.5 12.5C10.6326 12.5 10.7598 12.4473 10.8536 12.3536C10.9473 12.2598 11 12.1326 11 12V6Z"
                                        fill="#A3A3A3"
                                />
                                <path
                                        fill-rule="evenodd"
                                        clip-rule="evenodd"
                                        d="M14.5 3C14.5 3.26522 14.3946 3.51957 14.2071 3.70711C14.0196 3.89464 13.7652 4 13.5 4H13V13C13 13.5304 12.7893 14.0391 12.4142 14.4142C12.0391 14.7893 11.5304 15 11 15H5C4.46957 15 3.96086 14.7893 3.58579 14.4142C3.21071 14.0391 3 13.5304 3 13V4H2.5C2.23478 4 1.98043 3.89464 1.79289 3.70711C1.60536 3.51957 1.5 3.26522 1.5 3V2C1.5 1.73478 1.60536 1.48043 1.79289 1.29289C1.98043 1.10536 2.23478 1 2.5 1H6C6 0.734784 6.10536 0.48043 6.29289 0.292893C6.48043 0.105357 6.73478 0 7 0L9 0C9.26522 0 9.51957 0.105357 9.70711 0.292893C9.89464 0.48043 10 0.734784 10 1H13.5C13.7652 1 14.0196 1.10536 14.2071 1.29289C14.3946 1.48043 14.5 1.73478 14.5 2V3ZM4.118 4L4 4.059V13C4 13.2652 4.10536 13.5196 4.29289 13.7071C4.48043 13.8946 4.73478 14 5 14H11C11.2652 14 11.5196 13.8946 11.7071 13.7071C11.8946 13.5196 12 13.2652 12 13V4.059L11.882 4H4.118ZM2.5 3V2H13.5V3H2.5Z"
                                        fill="#A3A3A3"
                                />
                            </svg>
                        </button>
                    </li>
        `;
        productContainer.innerHTML += html
        changeCartItemQuantity()
        removeItemFromCartEvent()
    })
    totalPrice.textContent = `${data.total_price} AMD`
}

function renderProductInCheckoutPage(data) {
    const productContainer = document.querySelector('.payment__content_products-items');
    if (!productContainer) return;
    const totalPrice = document.querySelector('.payment__content_price')
    Object.values(data.cart).map(item => {
        const html = `
                <li class="payment__content_products-item">
                   <span>${item.product.name} (${item.quantity})</span>
                   <span class="line"></span>
                   <span>${item.price} AMD</span>
               </li>
        `;
        productContainer.innerHTML += html
    })
    totalPrice.innerHTML = +data.total_price + 600;
}


function removeItemFromCart(productId, productSize) {
    fetch(`${API_URL}/cart/remove/${productId}/${productSize}/`)
        .then(j => j.json())
        .then(data => {
            getCartItems(`${API_URL}/cart`)
                .then(data => {
                    cartRender(data)
                })
        }).catch(err => {
        console.log(err)
    })
}

function removeItemFromCartEvent() {
    const buttons = document.querySelectorAll('.cart__content_product-trash')
    buttons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            removeItemFromCart(btn.dataset.productId, btn.dataset.productSize)
        })
    })

}


function changeCartItemQuantity() {
    const quantity = document.querySelectorAll('.cart__item_quantity')
    quantity.forEach(item => {
        item.addEventListener('input', (e) => {
            if (+e.target.value <= 0) {
                removeItemFromCart(e.target.dataset.productId, e.target.dataset.size)
                return
            }
            const data = {
                quantity: e.target.value,
                update: true,
                size: e.target.dataset.size
            }
            addToCart(data, e.target.dataset.productId)
        })
    })
}

function addToCartEvent() {
    const buttons = document.querySelectorAll('.product__price');
    buttons.forEach(b => {
        const counter = b.parentElement.parentElement.querySelector('.product__count input')
        const notes = b.parentElement.parentElement.querySelector('.product__notes textarea')
        b.addEventListener('click', (e) => {
            const data = {
                quantity: +counter.value,
                notes: notes.value,
                update: false,
                size: e.target.dataset.size
            }
            addToCart(data, e.target.dataset.id)
            notes.value = ''
        })
    })
}

function addToCart(data, productId) {
    data.lang = window.location.pathname.match(/^\/[a-zA-Z]{2}\//)[0].split('/')[1];
    fetch(`${API_URL}/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            getCartItems(`${API_URL}/cart`)
                .then(data => {
                    cartRender(data)
                })
        }).catch(e => {
        console.log(e)
    })
}

addToCartEvent()

function checkout() {
    const form = document.querySelector('.payment__content_form');

    form.addEventListener('submit', (e) => {
        e.preventDefault()
        const fetchData = {}
        const data = [...(new FormData(form))];
        for ([key, val] of data) {
            console.log(key, val)
            fetchData[key] = val
        }
        fetch(`${API_URL}/payment/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(fetchData)
        })
            .then(res => res.json())
            .then(data => {
                if (data.status) {
                    console.log(data.url)
                    // window.location.href = data.url
                }
            }).catch(e => {
            console.log(e)
        })
        console.log(fetchData)
    })

}

// checkout()

function sendMail() {
    fetch(`${API_URL}/mail/`, {
        method: 'POST',
        body: JSON.stringify({data: true})
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        }).catch(err => {
        console.log(err)
    })
}

sendMail()