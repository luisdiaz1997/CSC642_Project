var eventBus = new Vue()

Vue.component('my-cart', {
  delimiters: ['[[',']]'],
  props: {
    orders: {
      type: Array,
      required: true
    }
  },
  template:  `

  <div class="card-body cart">
    <h5>Your Order</h5>
    <ul>
      <li v-for="order in orders">
        <h6>[[order.name]]</h6>
        <h6>Amount: [[order.number]]</h6>
        <h6>Sauce: [[order.sauce]]</h6>
        <h6 v-if="order.cheese">Cheese: [[order.cheese]]</h6>
        <h6 v-else>Cheese: none</h6>
        <h6>Extras:</h6>
        <ul>
          <li v-for="(i, extra) in order.extras" v-if="i">
            [[extra]]
          </li>
        </ul>

      </li>
    </ul>



  </div>

  `

})





var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
      cart: [],
    }
})
