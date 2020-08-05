Vue.component('assemble-cards', {
  delimiters: ['[[',']]'],
  props: {
    restaurant_data: {
      type: Array,
      required: true
    }
  },
  template: `
  <div>
  <ul>
    <li v-for="restaurant in restaurant_data">
      <p>[[restaurant.name]]</p>
    </li>
  </ul>

  </div>`
})

Vue.component('build-card', {
  delimiters: ['[[',']]'],
  props:{
    name: {
      type: String,
      required: true
    },
    im_src: {
      type: String,
      default: ''
    },
    img_style: {
      type: String,
      default: ''

    },
    card_style:{
      type: String,
      default: ''

    },
    rating:{
      type: Number,
      default: 0
    },
    size:{
      type: String,
      default: 'small'
    },
    discount:{
      type: String,
      default: 'False'
    },
    address:{
      type: String,
      default: ''
    }
  },
  template: `
  <div :class="'card bg-dark text-white ' + card_style" @mouseover="hoverCard(true)" @mouseout="hoverCard(false)">

    <img :src="im_src" class="card-img" :class="{img_style, 'selected': isSelected}" alt="...">

    <div class="card-img-overlay">
      <div class="card-title">
        <h3 v-if="size==='big'">
        [[name]] <add-stars :rating="rating"></add-stars>
        </h3>
        <h5 v-else>
        [[name]] <add-stars :rating="rating"></add-stars>
        </h5>
        <div v-if="address">
        [[address]]
        </div>
        <span v-if="discount==='True'">
        <button type="button" class="btn btn-primary btn-sm promo">Student Discount</button>
        </span>
      </div>
      <a href="/lorempizzeria" class="stretched-link"></a>
    </div>

  </div>
  `,
  data(){
    return{
      isSelected: false,
    }
  },
  methods:{
    hoverCard(state){
      this.isSelected= state //either true or false
    }
  }
})


Vue.component('add-stars',{
  delimiters: ['[[',']]'],
  props:{
    rating:{
      type: Number,
      default: 0
    }
  },
  template: `
  <span style="display:inline-block">
      <span v-for="n in parseInt(rating)">
      <svg class="bi" width="17" height="17" fill="currentColor">
        <use xlink:href="/static/node_modules/bootstrap-icons/bootstrap-icons.svg#star-fill"/>
      </svg>
      </span>

      <svg v-for="n in parseInt(5-rating)" class="bi" width="17" height="17" fill="currentColor">
        <use xlink:href="/static/node_modules/bootstrap-icons/bootstrap-icons.svg#star"/>
      </svg>
  </span>
  `
})

var app = new Vue({
  el: '#app',
  delimiters: ['[[',']]'],
  data:{

  }
})
