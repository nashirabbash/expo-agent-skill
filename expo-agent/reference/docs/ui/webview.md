---
title: "react-native-webview"
description: "A library that provides a WebView component."
source_url: "https://docs.expo.dev/versions/latest/sdk/webview.md"
scraped_at: "2026-07-15T08:45:17.922301"
---

---
title: react-native-webview
description: A library that provides a WebView component.
sourceCodeUrl: 'https://github.com/react-native-webview/react-native-webview'
packageName: react-native-webview
platforms: ['android', 'ios', 'expo-go']
inExpoGo: true
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# react-native-webview

A library that provides a WebView component.
Android, iOS, Included in Expo Go

`react-native-webview` provides a `WebView` component that renders web content in a native view.

## Installation

```sh
# npm
npx expo install react-native-webview

# yarn
yarn expo install react-native-webview

# pnpm
pnpm expo install react-native-webview

# bun
bun expo install react-native-webview
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project. Then, follow the [installation instructions](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Getting-Started.md#react-native-webview-getting-started-guide) provided in the library's README or documentation.

## Usage

```jsx
import { WebView } from 'react-native-webview';
import Constants from 'expo-constants';
import { StyleSheet } from 'react-native';

export default function App() {
  return (
    <WebView
      style={styles.container}
      source={{ uri: 'https://expo.dev' }}
    />
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: Constants.statusBarHeight,
  },
});
```

### With inline HTML

```jsx
import { WebView } from 'react-native-webview';
import Constants from 'expo-constants';
import { StyleSheet } from 'react-native';

export default function App() {
  return (
    <WebView
      style={styles.container}
      originWhitelist={['*']}
      source={{ html: '<h1><center>Hello world</center></h1>' }}
    />
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: Constants.statusBarHeight,
  },
});
```

## Learn more

[Visit official documentation](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Guide.md) — Get full information on API and its usage.
