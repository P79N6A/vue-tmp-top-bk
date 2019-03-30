<template>
    <div id="header-menu">
        <el-menu :default-active="defaultActive" class="el-menu-demo" mode="horizontal" @select="handleSelect"
                 text-color="#333"
                 active-text-color="#37b9ed"
                 router

        >
            <el-menu-item :index="menu_1.url" v-for="(menu_1, index) in menuOption.data" :key="index"
                          v-if="!menu_1.children">{{menu_1.displayName}}
            </el-menu-item>
            <el-submenu :index="'-1'" v-for="(menu_1, index) in menuOption.data" :key="index"
                        v-if="menu_1.children">
                <template slot="title">{{menu_1.displayName}}</template>
                <el-menu-item :index="menu_2.url" v-for="(menu_2,index) in menu_1.children" :key="index"
                              v-if="!menu_2.children">{{menu_2.displayName}}
                </el-menu-item>
                <el-submenu :index="'-1'" v-for="(menu_2,index) in menu_1.children" :key="index"
                            v-if="menu_2.children">
                    <template slot="title">{{menu_2.displayName}}</template>
                    <el-menu-item :index="menu_3.url" v-for="(menu_3,index) in menu_2.children" :key=index>
                        {{menu_3.displayName}}
                    </el-menu-item>
                </el-submenu>
            </el-submenu>
        </el-menu>
    </div>
</template>
<script>
    export default {
        name: 'headerMenu',
        props: {
            menuOption: {}
        },
        data() {
            return {
                defaultActive: '/home',
            };
        },
        created() {
            this.defaultActive = this.$route.path;
            console.log(this.defaultActive);
        },
        methods: {
            handleSelect(key, keyPath) {
                // console.log(key, keyPath);
            }
        }
    }
</script>
<style lang="scss" scoped>
    $headerHeight: 60px;
    #header-menu {
        height: $headerHeight;
        width: 100%;
        margin-left: 20px;
    }
</style>
