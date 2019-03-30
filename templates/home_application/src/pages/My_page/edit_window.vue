<template>
    <div>
        <el-dialog :title='showUserData.title' :visible.sync="showUserData.show" width="30%" center>
            <el-form v-model="showUserData.data" label-position="right" label-width="80px">
                <el-form-item label="姓名">
                    <el-input v-model="showUserData.data.name"></el-input>
                </el-form-item>
                <el-form-item label="年龄">
                    <el-input v-model="showUserData.data.age"></el-input>
                </el-form-item>
                <el-form-item label="性别">
                    <el-radio-group v-model="showUserData.data.sex">
                        <el-radio label="女" value="0"></el-radio>
                        <el-radio label="男" vlaue="1"></el-radio>
                    </el-radio-group>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="confirm()" size="small">保存</el-button>
                <el-button @click="cancel()" size="small">取 消</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: 'edit_window',
        props: {
            showUserData: {
            }
        },
        methods: {
            confirm () {
                if (this.showUserData.operation === 'add') {
                    this.add();
                }
                if (this.showUserData.operation === 'edit') {
                    this.edit();
                }
                this.showUserData.show = false;
            },
            cancel () {
                this.showUserData.show = false;
            },
            add () {
                this.$http.post('CreateUser', this.showUserData.data).then(res => {
                    if (res.result) {
                        this.showUserData.data.id = res.data.id;
                        this.$emit('save', this.showUserData);
                        this.$message({
                            message: '添加成功',
                            type: 'success'
                        });
                        //this.showUserData.data = {};//清空上一次添加的用户信息
                    }
                })
            },
            edit() {
                this.$http.post('EditUser', this.showUserData.data).then(res => {
                    if(res.result) {
                        this.$emit('save', this.showUserData);
                        this.$message({
                            message: '修改成功',
                            type: 'success'
                        })
                    }else {
                        alert('修改失败');
                    }
                })
            }
        }
    }

</script>

<style lang="scss" scoped>
    .dialog-content {
        text-align: left;
        width: 100%;
        margin: auto;
    }
</style>
