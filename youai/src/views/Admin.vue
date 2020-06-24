<template>
  <div class="admin">
    <el-container>
      <el-header>
        <el-menu
          :default-active="'1'"
          class="el-menu-demo"
          mode="horizontal"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item index="1">有爱四班</el-menu-item>
        </el-menu>
      </el-header>
      <el-container>
        <el-aside width="260px">
          <el-menu
            default-active="/admin/user"
            class="el-menu-vertical-demo"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#66ccff"
            router
          >
            <el-menu-item index="/admin/user">
              <i class="el-icon-setting"></i>
              <span slot="title">我的信息</span>
            </el-menu-item>
            <el-menu-item index="/admin/info">
              <i class="el-icon-setting"></i>
              <span slot="title">详细信息</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-container>
          <el-main>
            <router-view />
          </el-main>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'admin',
  mounted () {
    let token = localStorage.getItem('token')
    if (!token) {
      this.$router.push({ name: 'Auth' })
    }
  }
}
</script>

<style>
.admin {
  width: 100%;
  height: 100%;
}
.el-container {
  height: 100%;
}
.el-header {
  background-color: #545c64;
  text-align: center;
  line-height: 60px;
  padding: 0 !important;
}

.el-aside {
  width: 200px;
}
.el-main {
  background-color: #fff;
}
.el-menu {
  height: 100%;
  margin: 0;
}
</style>