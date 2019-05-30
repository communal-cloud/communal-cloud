<template>
    <div>
        <div class="kt-subheader kt-grid__item" id="kt_subheader">
            <div class="kt-subheader__main">
                <h3 class="kt-subheader__title">Welcome to Community Cloud!</h3>
            </div>
        </div>
        <div class="kt-content kt-grid__item kt-grid__item--fluid">
            <b-row>
                <b-col>
                    <div class="alert alert-secondary alert-elevate fade show" role="alert">
                        <div class="alert-icon"><i class="fa fa-book-open kt-font-brand"></i></div>
                        <div class="alert-text text-left">
                            This application is about building communities that you like!
                            <br />
                            Here, you can create communities, assign roles to members, workflows full of tasks and much more!
                        </div>
                    </div>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                    <communities></communities>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                    <my-communities></my-communities>
                </b-col>
            </b-row>
        </div>
    </div>
</template>

<script>
    import Communities from './Communities.vue'
    import MyCommunities from './MyCommunities.vue'
    import store from '../store'

    export default {
        store: store,
        name: 'home',
        components: {
            Communities,
            MyCommunities
        }
    }
</script>
