import DefaultTheme from 'vitepress/theme'
import './custom.css'
import ValenceTable from './components/ValenceTable.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ValenceTable', ValenceTable)
  }
}
