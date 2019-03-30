<template>
    <div id="main-container">
        <div></div>
        <router-view/>
    </div>
</template>

<script>
    export default {
        name: 'container',
        mounted() {
        },
        methods: {}
    }
</script>

<style lang="scss" scoped>
    $headerHeight: 60px;
    #main-container {
        float: right;
        width: 100%;
        background: #f5f5f5;
        margin-top: $headerHeight;
        overflow: hidden;
    }
</style>
