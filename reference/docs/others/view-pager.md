---
title: "react-native-pager-view"
description: "A component library that provides a carousel-like view to swipe through pages of content."
source_url: "https://docs.expo.dev/versions/latest/sdk/view-pager.md"
scraped_at: "2026-07-15T08:44:28.735262"
---

---
title: react-native-pager-view
description: A component library that provides a carousel-like view to swipe through pages of content.
sourceCodeUrl: 'https://github.com/callstack/react-native-pager-view'
packageName: react-native-pager-view
platforms: ['android', 'ios', 'expo-go']
inExpoGo: true
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# react-native-pager-view

A component library that provides a carousel-like view to swipe through pages of content.
Android, iOS, Included in Expo Go

> [`@expo/ui` provides a drop-in replacement](/versions/latest/sdk/ui/drop-in-replacements/pagerview.md) for `react-native-pager-view`, powered by Jetpack Compose on Android and SwiftUI on iOS.

`react-native-pager-view` exposes a component that provides the layout and gestures to scroll between pages of content, like a carousel.

## Installation

```sh
# npm
npx expo install react-native-pager-view

# yarn
yarn expo install react-native-pager-view

# pnpm
pnpm expo install react-native-pager-view

# bun
bun expo install react-native-pager-view
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project. Then, follow the [installation instructions](https://github.com/callstack/react-native-pager-view#linking) provided in the library's README or documentation.

## Example

```jsx
import { StyleSheet, View, Text } from 'react-native';
import PagerView from 'react-native-pager-view';

export default function MyPager() {
  return (
    <View style={styles.container}>
      <PagerView style={styles.container} initialPage={0}>
        <View style={styles.page} key="1">
          <Text>First page</Text>
          <Text>Swipe ➡️</Text>
        </View>
        <View style={styles.page} key="2">
          <Text>Second page</Text>
        </View>
        <View style={styles.page} key="3">
          <Text>Third page</Text>
        </View>
      </PagerView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  page: {
    justifyContent: 'center',
    alignItems: 'center',
  },
});
```

## Learn more

[Visit official documentation](https://github.com/callstack/react-native-pager-view) — Get full information on API and its usage.
