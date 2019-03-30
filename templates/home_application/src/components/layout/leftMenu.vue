<template>
    <div id="left-menu">
        left menu
    </div>
</template>

<script>
    export default {
        name: 'leftMenu'
    }
</script>

<style lang="scss" scoped>
    $headerHeight: 60px;
    #left-menu {
        width: 15%;
        background: #f00;
        min-width: 220px;
        height: calc(100% - 60px);
    }
</style>
