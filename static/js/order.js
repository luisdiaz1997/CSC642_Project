Vue.component('my-card', {
  delimiters: ['[[',']]'],
  props: {
    restaurant_data: {
      type: Array,
      required: true
    }
  },
  template: ``

})
Vue.component('my-modal', {
  delimiters: ['[[',']]'],
  props: {
    restaurant_data: {
      type: Array,
      required: true
    }
  },
  template: ``

})
Vue.component('my-cart', {
  delimiters: ['[[',']]'],
  props: {
    restaurant_data: {
      type: Array,
      required: true
    }
  },
  template: ``

})





var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
      products: [
            {id:1, quantity:1, name:"Make-Your-Own", image: 'static/images2/Make-Your-Own.jpg', price: 1199},
            {id:2, quantity:1, name:"Classic Cheese", image: 'static/images2/Classic Cheese.jpg', price: 1199},
            {id:3, quantity:1, name:"Meat Lovin", image: 'static/images2/Meat Lovin Pizza.jpg', price: 1199},
            {id:4, quantity:1, name:"BBQ Chicken", image: 'static/images2/BBQ Chicken.jpg', price: 1199},
            {id:5, quantity:1, name:"Hawt Dog", image: 'static/images2/Hawt Dog.jpg', price: 1199},
            {id:6, quantity:1, name:"Protein-Style", image: 'static/images2/Protein-Style.jpg', price: 1199},
            {id:7, quantity:1, name:"One-top Pizza", image: 'static/images2/One-top Pizza.jpg', price: 1199},
            {id:8, quantity:1, name:"Two-top Pizza", image: 'static/images2/Two-top Pizza.jpg', price: 1199}
            ],
      cart: [],
    },
      methods: {
        addToCart(product){
          this.cart.push(product);
        },

        }
})
