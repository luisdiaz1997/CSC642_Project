var eventBus = new Vue()

Vue.component('build-card', {
  delimiters: ['[[',']]'],
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  template: `
  <div class="card bg-dark text-white custom_cursor" @mouseover="hoverCard(true)" @mouseout="hoverCard(false)">
    <img :src="product.image" class="card-img-top" :class="{'selected': isSelected}">
    <div class="card-body">
      <h4 class="card-title">[[product.name]]</h4>
      <div class="card-text">$[[product.price/100]]</div>
      <a class="stretched-link" data-toggle="modal" :data-target="'#editModal'+product.id">
      </a>
    </div>
  </div>
  `,
  data(){
    return{
      isSelected: false
    }
  },
  methods:{
    hoverCard(state){
      this.isSelected= state //either true or false
    }
  }

})
Vue.component('my-modal', {
  delimiters: ['[[',']]'],
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  template: `
  <div class="modal fade" :id="'editModal' +product.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Customize [[product.name]]</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <div class="modal-body">
          <form>
            <div class="form-group form-check">
              <label for="item-name"></label>
              <h5 class="topping-title">Sauce</h5>
              <section>
               <div class="form-check">
                 <input type="radio" class="form-check-input with-gap" id="radioGap1" name="groupOfRadioGap" v-model="sauce" value="Red Sauce">
                 <label class="form-check-label" for="radioGap1">Red Sauce</label>
               </div>
               <div class="form-check">
                 <input type="radio" class="form-check-input with-gap" id="radioGap2" name="groupOfRadioGap" v-model="sauce" value="Pesto Sauce">
                 <label class="form-check-label" for="radioGap2">Pesto Sauce</label>
               </div>

               <div class="form-check">
                 <input type="radio" class="form-check-input with-gap" id="radioGap3" name="groupOfRadioGap" v-model="sauce" value="White Sauce">
                 <label class="form-check-label" for="radioGap3">White Sauce</label>
               </div>
              </section>

              <!-- Cheese Section -->
              <h5 class="topping-title">Cheese</h5>
              <section>
                 <div class="form-check">
                     <input type="radio" class="form-check-input" id="radioGap4" v-model="cheese" name="groupOfRadioCheese" value="Mozarella">
                     <label class="form-check-label" for="radioGap4">Mozarella</label>
                 </div>
              </section>

              <!-- Extra Section -->
              <h5 class="topping-title">Extras</h5>
              <section>
                 <div class="checkbox">
                     <label><input type="checkbox" v-model="extras.cheese"> Cheese</label>
                   </div>
                   <div class="checkbox">
                     <label><input type="checkbox" v-model="extras.toppings"> Toppings</label>
                   </div>
                   <div class="checkbox">
                     <label><input type="checkbox" v-model="extras.everything"> Everything</label>
                   </div>
              </section>
            </div>


            <form class="quantity">
              <h5>Quantity</h5>
              <div class="value-button" id="decrease" @click="decreasenumber" value="Decrease Value">-</div>
              <input type="number" id="number" v-model.number="number" />
              <div class="value-button" id="increase" @click="number++" value="Increase Value">+</div>
            </form>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary on" @click="addToCart">[[isInCart ? 'Added to cart': 'Add to Cart']]</button>
        </div>
      </div>
    </div>
  </div>
  `,
  data(){
    return{
      number: 1,
      extras:{
        cheese: '',
        toppings: '',
        everything: '',
      },
      cheese: '',
      sauce: '',
      isInCart: false,

    }
  },
  methods:{
    addToCart(){
      if (this.isInCart){
        return
      }
      let order = {
        name: this.product.name,
        number: this.number,
        extras:{
            cheese:this.extras.cheese,
            toppings:this.extras.toppings,
            everything: this.extras.everything,
        },
        cheese: this.cheese,
        sauce: this.sauce
      }
      this.isInCart=true,
      eventBus.$emit('order-sent', order)
      console.log(order)
    },
    decreasenumber(){
      if (this.number>1){
        this.number--
      }
    }
  }

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


    mounted(){
      eventBus.$on('order-sent', order => {
        this.cart.push(order)
      })
    }
})
