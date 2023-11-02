import { useState } from 'react'
import NavigationSection from './components/NavigationSection'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavigationSection />
    </>
  )
}

export default App
