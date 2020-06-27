<template>
  <div
    class="info"
    v-loading="loading"
    element-loading-text="拼命加载中"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
  >
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="姓名">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="性别">
        <el-radio-group v-model="form.sex">
          <el-radio :label="'男'">男</el-radio>
          <el-radio :label="'女'">女</el-radio>
          <el-radio :label="null">未知</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="年龄">
        <el-input-number v-model="form.age" :min="1" :max="100" label="年龄"></el-input-number>
      </el-form-item>
      <el-form-item label="生日">
        <el-date-picker v-model="form.birthday" type="date" placeholder="选择生日"></el-date-picker>
      </el-form-item>
      <el-form-item label="展示图片">
        <el-input v-model="form.image"></el-input>
        <el-upload
          class="avatar-uploader"
          :action="url + '/upload/'"
          :headers="headers"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="form.image" :src="form.image" class="avatar" />
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="展示介绍">
        <el-input type="textarea" :rows="3" placeholder="请输入详细信息" v-model="form.introduce"></el-input>
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
        <mavon-editor
          ref="markdownEditor"
          @save="updata"
          @imgAdd="imgAdd"
          :ishljs="true"
          v-model="form.info"
        ></mavon-editor>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="updata">更新</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
export default {
  name: "info",
  components: {
    'mavon-editor': mavonEditor
  },
  data () {
    return {
      form: {},
      headers: { token: localStorage.getItem("token") },
      loading: false,
      url: this.url
    };
  },
  methods: {
    imgAdd (pos, $file) {
      var formdata = new FormData();
      formdata.append('file', $file);
      this.axios({
        url: this.url + "/upload/",
        method: 'post',
        data: formdata,
        headers: {
          'Content-Type': 'multipart/form-data',
          'token': localStorage.getItem('token')
        },
      }).then((res) => {
        this.$refs.markdownEditor.$img2Url(pos, res.data.data.url);
      }).catch(err => {
        this.$message.error(err.message);
      })
    },
    beforeAvatarUpload () {
      this.loading = true;
    },
    handleAvatarSuccess (res) {
      this.loading = false;
      if (res.code === 200) {
        this.form.image = res.data.url;
        this.$message({
          message: res.msg,
          type: "success"
        });
      } else {
        this.$message.error(res.msg);
      }
    },
    updata () {
      this.loading = true;
      this.axios
        .post(this.url + "/admin/", this.form)
        .then(res => {
          if (res.data.code === 200) {
            this.$message({
              message: res.data.msg,
              type: "success"
            });
          } else {
            this.$message.error(res.data.msg);
          }
          this.loading = false;
        })
        .catch(err => {
          this.$message.error(err.message);
          this.loading = false;
        });
    },
    get () {
      this.loading = true;
      this.axios
        .get(this.url + "/admin/")
        .then(res => {
          if (res.data.code === 200) {
            this.form = res.data.data;
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
  },
  mounted () {
    let token = localStorage.getItem("token");
    if (token) {
      let user = token.split(".")[1];
      let userObj = JSON.parse(decodeURIComponent(escape(window.atob(user))));
      if (userObj.exp < new Date().getTime() / 1000) {
        localStorage.clear();
        this.$router.push({ name: "Auth" });
      } else {
        this.get();
      }
    }
  }
};
</script>

<style>
.info {
  padding: 20px;
}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  /* width: 178px; */
  max-height: 178px;
  display: block;
}
</style>