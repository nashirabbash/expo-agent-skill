---
title: "useNativeState"
description: "A React hook that creates observable state shared between JavaScript and native SwiftUI views."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/usenativestate.md"
scraped_at: "2026-07-15T08:59:24.564405"
---

---
title: useNativeState
description: A React hook that creates observable state shared between JavaScript and native SwiftUI views.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui/src/State/useNativeState.ts'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# useNativeState

A React hook that creates observable state shared between JavaScript and native SwiftUI views.
iOS, tvOS, Included in Expo Go

`useNativeState` returns an [`ObservableState`](/versions/latest/sdk/ui/swift-ui/usenativestate.md#observablestate) that maps to a SwiftUI [`ObservableObject`](https://developer.apple.com/documentation/combine/observableobject) on the native side, so reads and writes to `.value` are observed directly by SwiftUI without going through the React render cycle. This lets you update the native view synchronously from a worklet on the UI thread.

> **Note:** When working with the [React Compiler](https://react.dev/learn/react-compiler), you should refrain from accessing and modifying the `value` property directly. Instead, use the [`get`](/versions/latest/sdk/ui/swift-ui/usenativestate.md#observablestate) and [`set`](/versions/latest/sdk/ui/swift-ui/usenativestate.md#observablestate) methods, which are compliant with the React Compiler standards.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

> **Note:** Using worklets requires installing [`react-native-worklets`](https://docs.swmansion.com/react-native-worklets/) in your project. `useNativeState` itself works without it, but the synchronous UI-thread updates shown below depend on the worklet runtime.

The example below masks a phone number as the user types. The formatting and the writes to `maskedPhone.value` (text) and `selection.value` (cursor position) all happen synchronously on the UI thread, so there is no flicker between the typed value and the masked value.

```tsx
import { Host, TextField, useNativeState } from '@expo/ui/swift-ui';
import { keyboardType } from '@expo/ui/swift-ui/modifiers';
import { useEffectEvent } from 'react';

export default function WorkletPhoneMaskExample() {
  const maskedPhone = useNativeState('');
  const selection = useNativeState({ start: 0, end: 0 });

  const handleTextChange = useEffectEvent((v: string) => {
    'worklet';
    const digits = v.replace(/\D/g, '').slice(0, 10);
    let formatted: string;
    if (digits.length === 0) {
      formatted = '';
    } else if (digits.length <= 3) {
      formatted = digits;
    } else if (digits.length <= 6) {
      formatted = `(${digits.slice(0, 3)}) ${digits.slice(3)}`;
    } else {
      formatted = `(${digits.slice(0, 3)}) ${digits.slice(3, 6)}-${digits.slice(6)}`;
    }
    if (formatted !== v) {
      maskedPhone.value = formatted;
      // Snaps to end for demo. Real masks need smarter cursor handling.
      selection.value = { start: formatted.length, end: formatted.length };
    }
  });

  return (
    <Host matchContents>
      <TextField
        text={maskedPhone}
        selection={selection}
        placeholder="(555) 123-4567"
        modifiers={[keyboardType('phone-pad')]}
        onTextChange={handleTextChange}
      />
    </Host>
  );
}
```

## API

```tsx
import { useNativeState } from '@expo/ui/swift-ui';
```

## Hooks

### `useNativeState(initialValue)`

Supported platforms: iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `initialValue` | `T` |

  

Creates an observable native state that is automatically cleaned up when the component unmounts. `initialValue` is captured once on the first render

Returns: `ObservableState<t>`

## Types

### `ObservableState`

Supported platforms: iOS, tvOS.

Observable state shared between JavaScript and native views (Jetpack Compose on Android and SwiftUI on iOS).

Type: [SharedObject](/versions/v57.0.0/sdk/expo.md#sharedobjecttype) extended by:

| Property | Type | Description |
| --- | --- | --- |
| onChange | `[listener] | null` | A single listener invoked on the native UI runtime whenever the value changes (after iOS `didSet` and Android's setter). Assigning replaces the previous listener; assign `null` to clear. The initial value does not fire `onChange`. The callback must be a worklet so it can run synchronously on the UI thread. Attach it inside `useEffect` and clear it in the cleanup so the listener lifecycle matches the component lifecycle. . Example
```tsx
const state = useNativeState(0);

useEffect(() => {
  state.onChange = (value) => {
    'worklet';
    console.log('changed to', value);
  };
}, []);
```

 |
| value | `T` | The current value. Writes from a UI worklet are synchronous and immediately readable. Writes from the JS thread are scheduled to the UI thread asynchronously, the new value is not readable until the update has been applied. Prefer writing from a worklet when you need synchronous updates |
| get | `() => T` | Reads the current value. A React Compiler compliant alternative to reading `.value` |
| set | `(value: T) => void` | Writes a new value. A React Compiler-compliant alternative to assigning `.value` |
