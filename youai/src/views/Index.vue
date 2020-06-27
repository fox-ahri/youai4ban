<template>
  <div
    class="container"
    v-loading="loading"
    element-loading-text="拼命加载中"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
  >
    <div
      v-show="!loading"
      class="box"
      v-for="i in family"
      :key="i.id"
      @click="$router.push({name:'I', query:{id:i.id}})"
    >
      <el-image :src="i.image" lazy>
        <div slot="placeholder" class="image-slot">
          加载中
          <span class="dot">...</span>
        </div>
      </el-image>
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
  name: "Home",
  data () {
    return {
      family: [],
      loading: false
    };
  },
  methods: {
    disruption (data) {
      data.sort(() => 0.5 - Math.random());
      return data;
    }
  },
  mounted () {
    let token = localStorage.getItem("token");
    if (token) {
      let user = token.split(".")[1];
      let userObj = JSON.parse(decodeURIComponent(escape(window.atob(user))));
      if (userObj.exp < new Date().getTime() / 1000) {
        localStorage.clear();
      }
    }
    this.loading = true;
    this.axios
      .get(this.url + "/index/")
      .then(res => {
        if (res.data.code === 200) {
          this.family = this.disruption(res.data.data);
        } else {
          this.$message.error(res.data.msg);
        }
        this.loading = false;
      })
      .catch(err => {
        this.$message.error(err.message);
        this.loading = false;
      });
  }
};
</script>

<style scoped>
.el-image {
  width: 100%;
  height: 100%;
}
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
  cursor: pointer;
}
.container .box:hover .el-image {
  transform: scale(0.98);
}
.container .box:hover h2 {
  transform: scale(0.98);
}
.container .box:hover p {
  transform: scale(0.98);
}
.container .box .el-image  {
  max-width: 100%;
  transition: 0.2s;
}
.container .box h2 {
  margin: 10px 0 0;
  padding: 0;
  font-size: 20px;
  transition: 0.2s;
}
.container .box p {
  margin: 0;
  padding: 0 0 10px;
  font-size: 16px;
  transition: 0.2s;
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
