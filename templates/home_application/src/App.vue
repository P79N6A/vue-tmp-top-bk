<template>
    <div id='app'>
        <Header :menu-option="menuOption"></Header>
        <Container :style="{height: winHeight}"></Container>
    </div>
</template>

<script>
    import Header from '@/components/layout/header'
    import Container from '@/components/layout/container'
    import '@/assets/css/base.scss'
    import '@/assets/font/bkicon/style.css'
    export default {
        name: 'App',
        components: {
            Header,
            Container
        },
        created() {
            let headerHeight = 60;
            if (window.innerHeight) {
                this.winHeight = window.innerHeight;
            }
            if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth) {
                this.winHeight = document.documentElement.clientHeight;
            }
            this.winHeight = this.winHeight - headerHeight + 'px'
        },
        data() {
            return {
                menuOption: {
                    type: 'top',
                    data: [
                        {
                            displayName: '首页', iconClass: 'fa fa-tachometer fa-lg', url: '/'
                        },
                        {displayName: '蓝鲸考试', url: '/examination'},
                    ]
                }
            }
        }
    }
</script>
<style>
</style>
