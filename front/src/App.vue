<template>
    <v-app>
        <v-main class="content">
            <TruckMe/>
        </v-main>
    </v-app>
</template>

<script>
import TruckMe from './views/Truck-Me';

export default {
  name: 'App',

  components: {
    MSCRenderer,
  },

  data: () => ({
    //
  }),
};
</script>

<style lang="scss">
.content {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>