---
title: "SecureField"
description: "A SwiftUI SecureField component for password input."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/securefield.md"
scraped_at: "2026-07-15T08:59:26.880469"
---

---
title: SecureField
description: A SwiftUI SecureField component for password input.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# SecureField

A SwiftUI SecureField component for password input.
iOS, tvOS, Included in Expo Go

Expo UI SecureField matches the official SwiftUI [SecureField API](https://developer.apple.com/documentation/swiftui/securefield) and provides a text field that masks user input for passwords and other sensitive text.

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

### Basic secure field

```tsx
import { useState } from 'react';
import { Host, SecureField } from '@expo/ui/swift-ui';

export default function BasicSecureFieldExample() {
  const [password, setPassword] = useState('');

  return (
    <Host matchContents>
      <SecureField placeholder="Password" onTextChange={setPassword} />
    </Host>
  );
}
```

### Submit handling

Use the [`submitLabel`](/versions/latest/sdk/ui/swift-ui/modifiers.md#submitlabelsubmitlabel) and [`onSubmit`](/versions/latest/sdk/ui/swift-ui/modifiers.md#onsubmithandler) modifiers to handle form submission from the keyboard.

```tsx
import { useState } from 'react';
import { Host, SecureField } from '@expo/ui/swift-ui';
import { submitLabel, onSubmit } from '@expo/ui/swift-ui/modifiers';

export default function SecureFieldSubmitExample() {
  const [password, setPassword] = useState('');

  return (
    <Host matchContents>
      <SecureField
        placeholder="Password"
        onTextChange={setPassword}
        modifiers={[submitLabel('done'), onSubmit(() => console.log('Login submitted'))]}
      />
    </Host>
  );
}
```

### Imperative ref

Use a ref to imperatively set text, focus, or blur the secure field.

```tsx
import { useRef } from 'react';
import { Host, SecureField, SecureFieldRef, Button, HStack, VStack } from '@expo/ui/swift-ui';
import { buttonStyle } from '@expo/ui/swift-ui/modifiers';

export default function ImperativeSecureFieldExample() {
  const ref = useRef<SecureFieldRef>(null);

  return (
    <Host matchContents>
      <VStack>
        <SecureField ref={ref} placeholder="Password" />
        <HStack spacing={12}>
          <Button
            modifiers={[buttonStyle('bordered')]}
            onPress={() => ref.current?.focus()}
            label="Focus"
          />
          <Button
            modifiers={[buttonStyle('bordered')]}
            onPress={() => ref.current?.blur()}
            label="Blur"
          />
          <Button
            modifiers={[buttonStyle('bordered')]}
            onPress={() => ref.current?.setText('secret123')}
            label="Set Text"
          />
        </HStack>
      </VStack>
    </Host>
  );
}
```

## API

```tsx
import { SecureField } from '@expo/ui/swift-ui';
```

## Component

### `SecureField`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SecureFieldProps](#securefieldprops)\>

Renders a SwiftUI `SecureField` for password input.

SecureFieldProps

### `autoFocus`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean` • Default: `false`

If true, the secure field will be focused automatically when mounted.

### `children`

Supported platforms: iOS, tvOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Slot children - supports `<SecureField.Placeholder>` with a `<Text>` child

### `maxLength`

Supported platforms: iOS, tvOS.

Optional • Type: `number`

Maximum number of characters allowed. Truncates natively as the user types.

### `onFocusChange`

Supported platforms: iOS, tvOS.

Optional • Type: `(focused: boolean) => void`

A callback triggered when the field gains or loses focus.

### `onTextChange`

Supported platforms: iOS, tvOS.

Optional • Type: `(text: string) => void`

A callback triggered when the text value changes.

If the callback is marked with the `'worklet'` directive, it runs synchronously on the UI thread; otherwise it is delivered asynchronously as a regular JS event.

### `placeholder`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

A text that is displayed when the field is empty.

### `ref`

Supported platforms: iOS, tvOS.

Optional • Type: Ref<[SecureFieldRef](#securefieldref)\>

### `text`

Supported platforms: iOS, tvOS.

Optional • Type: [ObservableState](#observablestate)<string\>

An observable state that holds the current text. Create one with `useNativeState('')` or `useNativeState('initial value')`. If omitted, the field manages its own internal state.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)

## Types

### `SecureFieldRef`

Supported platforms: iOS, tvOS.

Can be used for imperatively setting text and focus on the `SecureField` component.

| Property | Type | Description |
| --- | --- | --- |
| blur | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |
| clear | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Clear the current text. |
| focus | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |
| setText | (newText: string) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |
