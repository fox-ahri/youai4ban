<template>
  <div class="info">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="姓名">
        <el-input v-model="form.number" disabled></el-input>
      </el-form-item>
      <el-form-item label="性别">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="年龄">
        <el-input v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item label="生日">
        <el-input v-model="form.avatar"></el-input>
      </el-form-item>
      <el-form-item label="展示图片">
        <el-input v-model="form.avatar"></el-input>
      </el-form-item>
      <el-form-item label="展示介绍">
        <el-input v-model="form.avatar"></el-input>
      </el-form-item>
      <el-form-item label="邮箱">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="手机">
        <el-input v-model="form.phone"></el-input>
      </el-form-item>
      <el-form-item label="QQ">
        <el-input v-model="form.qq"></el-input>
      </el-form-item>
      <el-form-item label="详细信息">
        <el-input v-model="form.info"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="updata">更新</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
/**
 * id = models.BigAutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=254, null=True)
    sex = models.CharField(max_length=10, null=True)
    age = models.SmallIntegerField(null=True)
    birthday = models.DateTimeField(null=True)
    image = models.CharField(max_length=254, null=True)
    introduce = models.TextField(null=True)
    info = models.TextField(null=True)
    email = models.CharField(max_length=254, null=True)
    phone = models.CharField(max_length=20, null=True)
    qq = models.CharField(max_length=20, null=True)
 */
export default {
  name: 'info',
  data () {
    return {
      form: {}
    }
  },
  methods: {
    updata () {
      if (this.form.password.trim().length < 1) {
        this.$message({
          message: '新密码不能为空',
          type: 'warning'
        })
        return
      }
      this.axios.put('http://127.0.0.1:9000/admin/', this.form).then(res => {
        if (res.data.code === 200) {
          localStorage.setItem('token', res.data.data.token)
          this.$message({
            message: res.data.msg,
            type: 'success'
          });
        } else {
          this.$message.error(res.data.msg);
        }
      }).catch(err => {
        this.$message.error(err.message);
      })
    }
  },
  mounted () {
    let token = localStorage.getItem('token')
    if (token) {
      let user = token.split('.')[1]
      let userObj = JSON.parse(decodeURIComponent(escape(window.atob(user))))
      if (userObj.exp < new Date().getTime() / 1000) {
        localStorage.clear()
        this.$router.push({ name: 'Auth' })
      }
    }
  }
}
</script>

<style>
</style>