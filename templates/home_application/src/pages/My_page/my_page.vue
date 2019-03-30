<template>
    <div>
        <div id="v-name">
            <div style="margin-top: 15px;margin-left: 10px" align="left">
                <el-input placeholder="输入姓名查询" v-model="search_name" style="width: 400px">
                    <el-button slot="append" icon="el-icon-search" @click="search()"></el-button>
                </el-input>
                <el-button type="success" @click="create_user()">添加用户</el-button>
            </div>
        </div>
        <div style="margin-top: 10px;margin-left: 10px;margin-right: 10px">
            <el-table :data="UserList" height="350" border style="width: 100%">
                <!--el-table-column prop="time_created" label="创建日期" width="300"></el-table-column-->
                <el-table-column type="index" label="序号" width="80"></el-table-column>
                <el-table-column prop="name" label="姓名"></el-table-column>
                <el-table-column prop="age" label="年龄"></el-table-column>
                <el-table-column prop="sex" label="性别"></el-table-column>
                <el-table-column label="操作" width="200">
                    <template slot-scope="scope">
                        <el-button type="primary" icon="el-icon-edit" @click="edit(scope.$index, scope.row)" circle>
                        </el-button>
                        <el-button type="danger" icon="el-icon-delete" @click="delete_user(scope.$index, scope.row)" circle>
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <edit-window :showUserData="UserInfo" @save="save"></edit-window>
    </div>
</template>

<script>
    import EditWindow from '@/pages/My_page/edit_window'

    export default {
        name: 'my_page',
        components: {
            EditWindow
        },
        data() {
            return {
                search_name: '',
                loading: false,
                UserInfo: {
                    show: false,
                    title: '',
                    operation: '',
                    data: {}
                },
                UserList: [],
            }
        },
        mounted() {
            this.search();
        },
        methods: {
            search() {
                this.loading = true;
                this.$http.post('SearchUser', {'name': this.search_name}).then(res => {
                    this.loading = false;
                    if (res.result) {
                        this.UserList = res.data;
                    }
                })
            },
            create_user() {
                this.UserInfo.show = true;
                this.UserInfo.title = '添加用户';
                this.UserInfo.operation = 'add';
                this.UserInfo.data = {};
            },
            edit(index, row) {
                this.UserInfo.show = true;
                this.UserInfo.title = '修改用户信息';
                this.UserInfo.operation = 'edit';
                this.UserInfo.index = index;
                this.UserInfo.data = JSON.parse(JSON.stringify(row))
                /*JSON.parse()将JSON数据转换成JS对象，
                JSON.stringify() 方法用于将 JavaScript 值转换为 JSON 字符串。*/
            },
            delete_user(index, row) {
                this.$confirm('确认删除？', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$http.post('DeleteUser?id' + row.id, {'id': row.id}).then(res => {
                        if (res.result) {
                            this.UserList.splice(index, 1);
                            this.$message({
                                message: '删除成功',
                                type: 'success'
                            })
                        }
                    })
                })
            },
            save(UserInfo) {
                if (UserInfo.operation === 'add') {
                    this.UserList.push(UserInfo.data)
                }
                if (UserInfo.operation === 'edit') {
                    this.UserList.splice(UserInfo.index, 1, UserInfo.data)
                    /*splice(index，len，item)用于数组的删除和替换，从index开始删，
                    删除len个；有item则是替换，用item替换掉index的数据*/
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    #log-manage {
        width: 100%;
        text-align: center;
        margin-top: 100px;
    }
</style>
