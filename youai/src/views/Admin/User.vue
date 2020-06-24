<template>
  <div class="user">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="学号">
        <el-input v-model="form.number" disabled></el-input>
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item label="头像">
        <el-input v-model="form.avatar"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="updata">更新</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'user',
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
      this.form = userObj
    }
  }
}
</script>

<style>
</style>