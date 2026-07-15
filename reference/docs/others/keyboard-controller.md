---
title: "react-native-keyboard-controller"
description: "A library that provides a Keyboard manager that works in an identical way on Android and iOS"
source_url: "https://docs.expo.dev/versions/latest/sdk/keyboard-controller.md"
scraped_at: "2026-07-15T08:45:02.888418"
---

---
title: react-native-keyboard-controller
description: A library that provides a Keyboard manager that works in an identical way on Android and iOS
sourceCodeUrl: 'https://github.com/kirillzyusko/react-native-keyboard-controller'
packageName: react-native-keyboard-controller
platforms: ['android', 'ios', 'expo-go']
inExpoGo: true
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# react-native-keyboard-controller

A library that provides a Keyboard manager that works in an identical way on Android and iOS
Android, iOS, Included in Expo Go

`react-native-keyboard-controller` offers additional functionality beyond the built-in React Native keyboard APIs, providing consistency across Android and iOS with minimal configuration and offering the native feel users expect.

## Installation

```sh
# npm
npx expo install react-native-keyboard-controller

# yarn
yarn expo install react-native-keyboard-controller

# pnpm
pnpm expo install react-native-keyboard-controller

# bun
bun expo install react-native-keyboard-controller
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project. Then, follow the [installation instructions](https://kirillzyusko.github.io/react-native-keyboard-controller/docs/installation) provided in the library's README or documentation.

## Usage

```tsx
import { TextInput, View, StyleSheet } from 'react-native';
import { KeyboardAwareScrollView, KeyboardToolbar } from 'react-native-keyboard-controller';

export default function FormScreen() {
  return (
    <>
      <KeyboardAwareScrollView bottomOffset={62} contentContainerStyle={styles.container}>
        <View>
          <TextInput placeholder="Type a message..." style={styles.textInput} />
          <TextInput placeholder="Type a message..." style={styles.textInput} />
        </View>
        <TextInput placeholder="Type a message..." style={styles.textInput} />
        <View>
          <TextInput placeholder="Type a message..." style={styles.textInput} />
          <TextInput placeholder="Type a message..." style={styles.textInput} />
          <TextInput placeholder="Type a message..." style={styles.textInput} />
        </View>
        <TextInput placeholder="Type a message..." style={styles.textInput} />
      </KeyboardAwareScrollView>
      <KeyboardToolbar />
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    gap: 16,
    padding: 16,
  },
  listStyle: {
    padding: 16,
    gap: 16,
  },
  textInput: {
    width: 'auto',
    flexGrow: 1,
    flexShrink: 1,
    height: 45,
    borderWidth: 1,
    borderRadius: 8,
    borderColor: '#d8d8d8',
    backgroundColor: '#fff',
    padding: 8,
    marginBottom: 8,
  },
});
```

## Additional resources

[Advanced keyboard handling](/guides/keyboard-handling.md#advanced-keyboard-handling-with-keyboard-controller) — Learn more about advanced keyboard handling examples with Keyboard Controller.

[Visit official documentation](https://kirillzyusko.github.io/react-native-keyboard-controller/) — Get full information on API and its usage.
