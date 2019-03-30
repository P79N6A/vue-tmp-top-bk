<template>
    <div>
        <!--<div style="margin: 10px">-->
        <!--<label>业务: </label>-->
        <!--<el-select v-model="biz_value" placeholder="请选择业务" style="width: 400px">-->
        <!--<el-option-->
        <!--v-for="item in biz_list"-->
        <!--:key="item.value"-->
        <!--:label="item.label"-->
        <!--:value="item.value">-->
        <!--</el-option>-->
        <!--</el-select>-->
        <!--</div>-->
        <div style="margin: 10px">
            <label>IP: </label>
            <el-input style="width: 200px;height: 40px" v-model="ip_input" placeholder="请输入IP"></el-input>
            <el-button type="primary" @click="searchHost">查询</el-button>
            <el-button type="primary" style="float: right;" @click="addHosts">新增主机</el-button>
        </div>
        <div style="margin: 10px">
            <el-table :data="hostInfo" height="450" border style="width: 100%">
                <el-table-column prop="bk_host_innerip" label="主机IP"></el-table-column>
                <el-table-column prop="bk_host_name" label="主机名"></el-table-column>
                <el-table-column prop="bk_host_name" label="所属业务"></el-table-column>
                <el-table-column prop="bk_cloud_name" label="云区域"></el-table-column>
                <el-table-column prop="bk_os_name" label="操作系统类型"></el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <div style="align-items: center">
                            <i class="el-icon-search" @click="searchInfo(scope.row)"></i>
                            <i class="el-icon-view" @click="addMonitor(scope.row)"></i>
                            <i class="el-icon-delete" @click="deleteMonitor(scope.row)"></i>
                            <el-button type="text">查看性能</el-button>
                        </div>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <div>
            <new-add :data="new_add"></new-add>
        </div>
    </div>
</template>

<script>
    import NewAdd from '@/pages/bk_examination/new_add'

    export default {
        name: 'examination',
        components: {
            NewAdd
        },
        data() {
            return {
                ip_input: '',
                biz_list: [],
                biz_value: '',
                hostInfoList: [],
                tableSize: 100,
                monitor: false,
                new_add: {
                    biz_list: [],
                    host_list: [],
                    isShow: false
                }
            }
        },
        created() {
            this.searchBiz()
        },
        methods: {
            searchHost() {
                let params = {};
                params['bk_biz_id'] = this.biz_value;
                params['bk_host_innerip'] = this.ip_input;
                this.loading = true;
                this.$http.post('search_host', params).then(res => {
                    this.loading = false;
                    if (res['result']) {
                        this.hostInfo = res.data
                    } else {
                        this.$message.error('查询主机失败' + res['bk_error_msg'])
                    }
                })
            },
            hostInfo() {
                this.loading = true;
                this.$http.post('host_info', {}).then(res => {
                    this.loading = false;
                    if (res['result']) {
                        this.hostInfoList = res.data
                    } else {
                        this.$message.error('查询主机失败' + res['bk_error_msg'])
                    }
                })
            },
            async addHosts() {
                this.new_add.biz_list = await this.searchBiz();
                this.new_add.host_list = await this.searchHost();
                this.new_add.isShow = true
            },
            searchBiz() {
                this.$http.post('search_biz', {}).then(res => {
                    this.biz_list = res.data;
                    return res.data
                })
            },
            searchInfo(item) {
                this.$http.post('search_info', item).then(res => {
                    if (res['result']) {
                        this.hostInfo = this.hostInfo.concat(res.data)
                    } else {
                        this.$message.error('查询主机使用率信息失败')
                    }
                })
            },
            // deleteMonitor(item) {
            //     let params = {};
            //     params['bk_host_id'] = item['bk_host_id'];
            //     this.$http.post('delete_monitor', params).then(res => {
            //         if (res['result']) {
            //             this.monitor = false;
            //             this.$message.success('删除监控成功')
            //         } else {
            //             this.$message.error('删除监控失败')
            //         }
            //     })
            // },
            // addMonitor(item) {
            //     this.$http.post('add_monitor', item).then(res => {
            //         if (res['result']) {
            //             this.monitor = true;
            //             this.$message.success('添加监控成功')
            //         } else {
            //             this.$message.error('添加监控失败')
            //         }
            //     })
            // },
        }
    }
</script>

<style scoped>

</style>
