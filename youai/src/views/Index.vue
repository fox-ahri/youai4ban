<template>
  <div class="container">
    <div class="box" v-for="i in family" :key="i.id">
      <img :src="i.img" :alt="i.name" />
      <h2>{{i.name}}</h2>
      <p>{{i.introduce}}</p>
    </div>
    <div class="box">
      <h1 @click="$router.push({ name: 'Admin' })">ADMIN</h1>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data () {
    return {
      family: []
    }
  },
  methods: {
    disruption (data) {
      data.sort(() => 0.5 - Math.random())
      return data
    },
    request () {
      let data = [{
        id: 1,
        img: "https://api.ahriknow.com/image?album=girl,1",
        name: "Lorem ipsum dolor",
        introduce: `Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit est
        veniam molestiae et aspernatur.`
      }, {
        id: 2,
        img: "https://api.ahriknow.com/image?album=girl,10",
        name: "Lorem ipsum dolor",
        introduce: `Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit est
        veniam molestiae et aspernatur, optio, vitae esse sequi eius
        temporibus deserunt possimus in totam distinctio! Iusto, iste? Magnam,
        illum esse, iste? Magnam, illum esse. iste? Magnam,
        illum esse, iste? Magnam, illum esse.`
      }, {
        id: 3,
        img: "https://api.ahriknow.com/image?album=girl,100",
        name: "Lorem ipsum dolor",
        introduce: `Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit est
        veniam molestiae et aspernatur, optio, vitae esse sequi eius
        temporibus deserunt possimus in totam distinctio! Iusto, iste? Magnam,
        illum esse, iste? Magnam, illum esse.`
      }, {
        id: 4,
        img: "https://api.ahriknow.com/image?album=girl,1000",
        name: "Lorem ipsum dolor",
        introduce: `Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit est
        veniam molestiae et aspernatur, optio, vitae esse sequi eius
        temporibus deserunt possimus in totam distinctio! Iusto, iste? Magnam,
        illum esse, iste? Magnam, illum esse. optio, vitae esse sequi eius
        temporibus deserunt possimus in totam distinctio! Iusto, iste? Magnam,
        illum esse, iste? Magnam, illum esse.`
      }, {
        id: 5,
        img: "https://api.ahriknow.com/image?album=girl,166",
        name: "Lorem ipsum dolor",
        introduce: `Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit est
        veniam molestiae et aspernatur, optio, vitae esse sequi eius
        temporibus deserunt possimus in totam distinctio! Iusto, iste? Magnam,
        illum esse, iste? Magnam, illum esse.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit est
        veniam molestiae et aspernatur, optio, vitae esse sequi eius
        temporibus deserunt possimus in totam distinctio! Iusto, iste? Magnam,
        illum esse, iste? Magnam, illum esse.`
      }]
      this.family = this.disruption(data)
    }
  },
  mounted () {
    this.request()
    let token = localStorage.getItem('token')
    if (token) {
      let user = token.split('.')[1]
      let userObj = JSON.parse(decodeURIComponent(escape(window.atob(user))))
      if (userObj.exp < new Date().getTime() / 1000) {
        localStorage.clear()
      }
    }
  }
}
</script>

<style scoped>
.container {
  width: 1200px;
  margin: 10px auto;
  columns: 4;
  column-gap: 40px;
  padding-bottom: 100px;
}
.container .box {
  width: 100%;
  margin: 0 0 20px;
  padding: 10px;
  background: #fff;
  overflow: hidden;
  break-inside: avoid;
}
.container .box img {
  max-width: 100%;
}
.container .box h2 {
  margin: 10px 0 0;
  padding: 0;
  font-size: 20px;
}
.container .box p {
  margin: 0;
  padding: 0 0 10px;
  font-size: 16px;
}
.container .box h1 {
  cursor: pointer;
  transition: 0.2s;
}
.container .box h1:hover {
  color: #2db9ff;
}

@media screen and (max-width: 1300px) {
  .container {
    columns: 3;
    width: calc(100% - 40px);
    box-sizing: border-box;
    padding: 20px 20px 20px 0;
  }
}
@media screen and (max-width: 768px) {
  .container {
    columns: 2;
  }
}
@media screen and (max-width: 480px) {
  .container {
    columns: 1;
  }
}
</style>
