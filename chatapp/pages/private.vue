<template>
    <v-app :style="{background: $vuetify.theme.themes[theme].background}">
    </v-app>
</template>

<script>
export default {
    computed: {
      theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    }
  },
    
}
</script>