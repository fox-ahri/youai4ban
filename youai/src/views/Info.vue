<template>
  <div
    class="infomation"
    v-loading="loading"
    element-loading-text="拼命加载中"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
  >
    <div class="back" @click="$router.go(-1)">
      <i class="el-icon-caret-left"></i>
    </div>
    <div class="base">
      <div class="image">
        <el-image :src="info.image" lazy>
          <div slot="placeholder" class="image-slot">
            加载中
            <span class="dot">...</span>
          </div>
        </el-image>
      </div>
      <div class="info">
        <table>
          <tr>
            <td class="c1">姓名:</td>
            <td class="c2">{{info.name}}</td>
          </tr>
          <tr>
            <td class="c1">性别:</td>
            <td class="c2">{{info.sex}}</td>
          </tr>
          <tr>
            <td class="c1">生日:</td>
            <td class="c2">{{info.birthday}}</td>
          </tr>
          <tr>
            <td class="c1">手机:</td>
            <td class="c2">{{info.phone}}</td>
          </tr>
        </table>
      </div>
    </div>
    <el-divider></el-divider>
    <div class="content">
      <div class="markdown-body" v-html="content"></div>
    </div>
  </div>
</template>

<script>
import '../assets/github-markdown.min.css'
const md = require('markdown-it')()
export default {
  name: 'infomation',
  data () {
    return {
      info: {},
      content: '',
      loading: false
    }
  },
  mounted () {
    this.loading = true
    this.axios
      .get(this.url + "/index/" + this.$route.query.id + "/")
      .then(res => {
        if (res.data.code === 200) {
          this.info = res.data.data;
          this.content = md.render(res.data.data.info)
        } else {
          this.$message.error(res.data.msg);
        }
        this.loading = false
      })
      .catch(err => {
        this.$message.error(err.message);
        this.loading = false
      });
  }
}
</script>

<style scoped>
.infomation {
  width: 1200px;
  background: #fff;
  margin: 60px auto;
  padding: 30px 0;
}
.infomation .back {
  position: fixed;
  top: 0;
  left: 0;
  height: 50px;
  width: 50px;
  text-align: center;
  line-height: 60px;
  background: #fff;
  font-size: 32px;
  cursor: pointer;
  transition: 0.2s;
}
.infomation .back:hover {
  background: #eee;
}
.infomation .base {
  display: flex;
  justify-content: flex-start;
  margin: 0 20px;
}
.infomation .base .image {
  width: 300px;
}
.infomation .base .image img {
  width: 100%;
  height: auto;
}
.infomation .base .info {
  padding: 6px 20px;
}
.infomation .base .info .c1 {
  font-size: 24px;
  font-weight: 600;
}
.infomation .base .info .c2 {
  font-size: 20px;
  padding-left: 20px;
}
.content {
  margin: 10px 100px;
}
.el-image {
  width: 100%;
  height: 100%;
}

@media screen and (max-width: 1300px) {
  .infomation {
    width: 90%;
  }
  .content {
    margin: 10px 30px;
  }
}
@media screen and (max-width: 768px) {
  .infomation {
    width: 90%;
  }
  .infomation .base {
    flex-direction: column;
  }
  .infomation .base .info {
    padding: 20px 0;
  }
}
@media screen and (max-width: 480px) {
  .infomation {
    width: 96%;
  }
  .infomation .base .image {
    width: 100%;
  }
}
</style>