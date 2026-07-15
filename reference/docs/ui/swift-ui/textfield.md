---
title: "TextField"
description: "A SwiftUI TextField component for text input."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/textfield.md"
scraped_at: "2026-07-15T08:59:41.527341"
---

---
title: TextField
description: A SwiftUI TextField component for text input.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# TextField

A SwiftUI TextField component for text input.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`TextInput`](/versions/latest/sdk/ui/universal/textinput.md) — it renders the appropriate native component per platform.

Expo UI TextField matches the official SwiftUI [TextField API](https://developer.apple.com/documentation/swiftui/textfield) and supports single-line and multiline input, keyboard configuration, submit handling, and an imperative `ref` for programmatic control.

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

### Uncontrolled text field

Bind a [`useNativeState`](/versions/latest/sdk/ui/swift-ui/usenativestate.md) observable to `text`. The field tracks the user's input on its own, and you read the current value from `textState.value`.

```tsx
import { Host, TextField, useNativeState } from '@expo/ui/swift-ui';

export default function BasicTextFieldExample() {
  const textState = useNativeState('');

  return (
    <Host matchContents>
      <TextField placeholder="Username" text={textState} />
    </Host>
  );
}
```

### Controlled text field

Pass an `onTextChange` worklet to transform or validate input and write the result back to the [`useNativeState`](/versions/latest/sdk/ui/swift-ui/usenativestate.md) observable state. The example below uppercases the text as it is typed.

> **Note:** Worklets require installing [`react-native-worklets`](https://docs.swmansion.com/react-native-worklets/).

```tsx
import { Host, TextField, useNativeState } from '@expo/ui/swift-ui';
import { useCallback } from 'react';

export default function ControlledTextFieldExample() {
  const text = useNativeState('');

  const handleTextChange = useCallback(
    (value: string) => {
      'worklet';
      text.value = value.toUpperCase();
    },
    [text]
  );

  return (
    <Host matchContents>
      <TextField placeholder="Name" text={text} onTextChange={handleTextChange} />
    </Host>
  );
}
```

### Multiline text field

Set `axis="vertical"` to allow the text field to expand vertically. Use the [`lineLimit`](/versions/latest/sdk/ui/swift-ui/modifiers.md#linelimit) modifier to control the visible line count. When using `Host matchContents`, add `fixedSize({ horizontal: false, vertical: true })` so the text field accepts the parent's width while using its ideal height.

```tsx
import { Host, TextField, useNativeState } from '@expo/ui/swift-ui';
import { lineLimit, fixedSize } from '@expo/ui/swift-ui/modifiers';

export default function MultilineTextFieldExample() {
  const textState = useNativeState('');

  return (
    <Host matchContents>
      <TextField
        axis="vertical"
        text={textState}
        placeholder="Tell us about yourself..."
        modifiers={[lineLimit(5), fixedSize({ horizontal: false, vertical: true })]}
      />
    </Host>
  );
}
```

### Keyboard type

Use the [`keyboardType`](/versions/latest/sdk/ui/swift-ui/modifiers.md#keyboardtypekeyboardtype) modifier to display a specific keyboard layout.

```tsx
import { Host, TextField, useNativeState } from '@expo/ui/swift-ui';
import { keyboardType, autocorrectionDisabled } from '@expo/ui/swift-ui/modifiers';

export default function KeyboardTypeExample() {
  const textState = useNativeState('');

  return (
    <Host matchContents>
      <TextField
        placeholder="Email"
        text={textState}
        modifiers={[keyboardType('email-address'), autocorrectionDisabled()]}
      />
    </Host>
  );
}
```

### Submit handling

Use the [`submitLabel`](/versions/latest/sdk/ui/swift-ui/modifiers.md#submitlabelsubmitlabel) modifier to customize the return key and [`onSubmit`](/versions/latest/sdk/ui/swift-ui/modifiers.md#onsubmithandler) to handle the submit action.

```tsx
import { Host, TextField, useNativeState } from '@expo/ui/swift-ui';
import { submitLabel, onSubmit } from '@expo/ui/swift-ui/modifiers';

export default function SubmitHandlingExample() {
  const textState = useNativeState('');

  return (
    <Host matchContents>
      <TextField
        placeholder="Search..."
        text={textState}
        modifiers={[
          submitLabel('search'),
          onSubmit(() => console.log('Submitted:', textState.value)),
        ]}
      />
    </Host>
  );
}
```

### Imperative ref

Use a `ref` to imperatively set text, focus, blur, or select text.

> **Note:** `setSelection` requires iOS 18.0+ / tvOS 18.0+. The other ref methods work on all supported versions.

```tsx
import { useRef } from 'react';
import {
  Host,
  TextField,
  TextFieldRef,
  Button,
  HStack,
  VStack,
  useNativeState,
} from '@expo/ui/swift-ui';
import { buttonStyle } from '@expo/ui/swift-ui/modifiers';

export default function ImperativeRefExample() {
  const ref = useRef<TextFieldRef>(null);
  const textState = useNativeState('Select me!');

  return (
    <Host matchContents>
      <VStack>
        <TextField ref={ref} text={textState} placeholder="Imperative field" />
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
            onPress={() => ref.current?.setText('SwiftUI rocks!')}
            label="Set Text"
          />
          <Button
            modifiers={[buttonStyle('bordered')]}
            onPress={() => ref.current?.clear()}
            label="Clear"
          />
          <Button
            modifiers={[buttonStyle('bordered')]}
            onPress={() => ref.current?.setSelection(0, 7)}
            label="Select"
          />
        </HStack>
      </VStack>
    </Host>
  );
}
```

### Worklet text masking

When `onTextChange` is marked with the `'worklet'` directive, it runs synchronously on the UI thread, so writes to [`useNativeState`](/versions/latest/sdk/ui/swift-ui/usenativestate.md) observables inside the callback take effect before the next frame. There is no flicker between the typed text and the masked text. The example below masks a phone number as the user types and writes both `text` and `selection` from the worklet to keep the cursor at the end of the formatted value.

> **Note:** Worklets require installing [`react-native-worklets`](https://docs.swmansion.com/react-native-worklets/). The `selection` prop requires iOS 18.0+ / tvOS 18.0+. On older versions the worklet can still update the text but cursor positioning is unavailable.

```tsx
import { Host, TextField, useNativeState } from '@expo/ui/swift-ui';
import { keyboardType } from '@expo/ui/swift-ui/modifiers';
import { useEffectEvent } from 'react';

export default function WorkletPhoneMaskExample() {
  const phone = useNativeState('');
  const selection = useNativeState({ start: 0, end: 0 });

  const handleTextChange = useEffectEvent((v: string) => {
    'worklet';
    const digits = v.replace(/\D/g, '').slice(0, 10);
    let formatted = digits;
    if (digits.length > 6) {
      formatted = `(${digits.slice(0, 3)}) ${digits.slice(3, 6)}-${digits.slice(6)}`;
    } else if (digits.length > 3) {
      formatted = `(${digits.slice(0, 3)}) ${digits.slice(3)}`;
    }
    if (formatted !== v) {
      phone.value = formatted;
      // Snaps to end for demo. Real masks need smarter cursor handling.
      selection.value = { start: formatted.length, end: formatted.length };
    }
  });

  return (
    <Host matchContents>
      <TextField
        text={phone}
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
import { TextField } from '@expo/ui/swift-ui';
```

## Component

### `TextField`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TextFieldProps](#textfieldprops)\>

Renders a SwiftUI `TextField`.

TextFieldProps

### `autoFocus`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean` • Default: `false`

If true, the text field will be focused automatically when mounted.

### `axis`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string` • Default: `'horizontal'`

The axis along which the text field grows when content exceeds a single line.

-   `'horizontal'` — single line (default).
-   `'vertical'` — expands vertically for multiline content. Use `lineLimit` modifier to cap visible lines.

Acceptable values are: `'vertical'` | `'horizontal'`

### `children`

Supported platforms: iOS, tvOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Slot children — supports `<TextField.Placeholder>` with a `<Text>` child (any text-styling modifiers on that `Text` are preserved as the placeholder's styling).

### `maxLength`

Supported platforms: iOS, tvOS.

Optional • Type: `number`

Maximum number of characters allowed. Truncates natively as the user types.

### `onFocusChange`

Supported platforms: iOS, tvOS.

Optional • Type: `(focused: boolean) => void`

A callback triggered when the field gains or loses focus.

### `onSelectionChange`

Supported platforms: iOS 18.0+ tvos 18.0+.

Optional • Type: `(selection: { end: number, start: number }) => void`

A callback triggered when the text selection range changes.

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

Optional • Type: Ref<[TextFieldRef](#textfieldref)\>

### `selection`

Supported platforms: iOS 18.0+ tvos 18.0+.

Optional • Type: [ObservableState](#observablestate)<[TextFieldSelection](#textfieldselection)\>

Observable state the field writes the current selection to. Create with `useNativeState<TextFieldSelection>({ start: 0, end: 0 })`. Use `ref.setSelection(start, end)` to set programmatically.

### `text`

Supported platforms: iOS, tvOS.

Optional • Type: [ObservableState](#observablestate)<string\>

An observable state that holds the current text. Create one with `useNativeState('')` or `useNativeState('initial value')`. If omitted, the field manages its own internal state.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)

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

### `TextFieldRef`

Supported platforms: iOS, tvOS.

Can be used for imperatively focusing and setting text/selection on the `TextField` component.

| Property | Type | Description |
| --- | --- | --- |
| blur | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |
| clear | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Clear the current text. |
| focus | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |
| setSelection | (start: number, end: number) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Supported platforms: iOS 18.0+ tvos 18.0+. Programmatically set the selection range. |
| setText | (newText: string) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |

### `TextFieldSelection`

Supported platforms: iOS, tvOS.

Selection range — `start` and `end` are character offsets into the field's text.

| Property | Type | Description |
| --- | --- | --- |
| end | `number` | - |
| start | `number` | - |
