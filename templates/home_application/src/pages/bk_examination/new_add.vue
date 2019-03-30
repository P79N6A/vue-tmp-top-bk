<template>
    <div>
        <el-dialog title='新增服务器' :visible.sync="data.isShow" width="40%" center>
            <div style="margin: 10px">
                <div>
                    <label>选择业务: </label>
                    <el-select v-model="biz_value" placeholder="请选择业务" style="width: 400px; margin-left: 10px">
                        <el-option
                            v-for="item in data.biz_list"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div style="margin-top: 10px">
                    <label>选择主机: </label>
                    <el-select v-model="biz_value" placeholder="请选择主机" style="width: 400px; margin-left: 10px">
                        <el-option
                            v-for="item in data.host_list"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </div>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="confirm()" size="small">保存</el-button>
                <el-button @click="cancel()" size="small">返回</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: 'new_add',
        props: {
            data: {}
        },
        methods: {
            // cancel() {
            //     this.isShow = false
            // },
            add() {
            }
        }
    }
</script>

<style scoped>

</style>
