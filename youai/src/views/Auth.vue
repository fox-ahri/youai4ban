<template>
  <div class="auth">
    <div class="form">
      <input class="input" type="text" v-model="userinfo.number" />
      <input class="input" type="password" v-model="userinfo.password" />
      <button class="button" @click="login">登录</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "auth",
  data() {
    return {
      userinfo: {
        number: "",
        password: ""
      }
    };
  },
  methods: {
    login() {
      this.axios
        .post(this.url + "/login/", this.userinfo)
        .then(res => {
          if (res.data.code === 200) {
            localStorage.setItem("token", res.data.data.token);
            this.$router.push({ name: "Index" });
          } else {
            this.$message.error(res.data.msg);
          }
        })
        .catch(err => {
          this.$message.error(err.message);
        });
    }
  }
};
</script>

<style scoped>
.form {
  margin: 120px auto;
  width: 300px;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.input {
  height: 32px;
  padding: 2px;
  border: solid 1px #999;
  background: none;
  color: #eee;
}
.button {
  height: 38px;
  cursor: pointer;
  border: none;
  background: #999;
  transition: 0.3s;
  color: #eee;
}
.button:hover {
  background: #666;
}

@media screen and (max-width: 800px) {
  .form {
    margin: 120px auto;
    width: 90%;
  }
}
</style>