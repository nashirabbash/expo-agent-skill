---
title: "TextInput"
description: "A text input backed by native SwiftUI and Jetpack Compose components, with a React Native-compatible API."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/textinput.md"
scraped_at: "2026-07-15T09:01:44.236984"
---

---
title: TextInput
description: A text input backed by native SwiftUI and Jetpack Compose components, with a React Native-compatible API.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# TextInput

A text input backed by native SwiftUI and Jetpack Compose components, with a React Native-compatible API.
Android, iOS, Web, Included in Expo Go

A text input that routes to [`TextField`](/versions/latest/sdk/ui/jetpack-compose/textfield.md) from `@expo/ui/jetpack-compose` on Android, [`TextField`](/versions/latest/sdk/ui/swift-ui/textfield.md) from `@expo/ui/swift-ui` on iOS, and React Native's [`TextInput`](https://reactnative.dev/docs/textinput) on web.

The API mirrors React Native's [`TextInput`](https://reactnative.dev/docs/textinput), with two changes: [`value`](/versions/latest/sdk/ui/universal/textinput.md#value) and [`selection`](/versions/latest/sdk/ui/universal/textinput.md#selection) are observable state objects (created with `useNativeState`), and [`onChangeText`](/versions/latest/sdk/ui/universal/textinput.md#onchangetext) can be a worklet for synchronously updating the state on the UI thread.

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

### Uncontrolled

Omit [`value`](/versions/latest/sdk/ui/universal/textinput.md#value) and the field manages its own text internally. Use [`onChangeText`](/versions/latest/sdk/ui/universal/textinput.md#onchangetext) to observe edits, and use the [ref](/versions/latest/sdk/ui/universal/textinput.md#textinputref) for imperative actions like `focus`, `blur`, and `clear`.

```tsx
import { Button, Column, Host, TextInput, type TextInputRef } from '@expo/ui';
import { useRef } from 'react';

export default function UncontrolledTextInputExample() {
  const inputRef = useRef<TextInputRef>(null);

  return (
    <Host matchContents={{ vertical: true }}>
      <Column spacing={8}>
        <TextInput
          ref={inputRef}
          defaultValue="hello"
          placeholder="Type here"
          onChangeText={value => console.log(value)}
        />
        <Button label="Clear" onPress={() => inputRef.current?.clear()} />
      </Column>
    </Host>
  );
}
```

### Controlled

Pass [`value`](/versions/latest/sdk/ui/universal/textinput.md#value) to drive the field from a `useNativeState` observable. The example below replaces `Hello` with `World` as you type.

```tsx
import { Host, TextInput, useNativeState } from '@expo/ui';
import { useCallback } from 'react';

export default function ControlledTextInputExample() {
  const text = useNativeState('');

  const handleChangeText = useCallback(
    (value: string) => {
      'worklet';
      text.value = value === 'Hello' ? 'World' : value;
    },
    [text]
  );

  return (
    <Host matchContents={{ vertical: true }}>
      <TextInput value={text} placeholder="Type here" onChangeText={handleChangeText} />
    </Host>
  );
}
```

### Worklet masking

Add the `'worklet'` directive to [`onChangeText`](/versions/latest/sdk/ui/universal/textinput.md#onchangetext) for synchronously updating the state on the UI thread. Writes to `value` land without the JS-thread round-trip that can cause cursor flicker.

> **Note:** Worklets require installing [`react-native-worklets`](https://docs.swmansion.com/react-native-worklets/).

```tsx
import { Host, TextInput, useNativeState } from '@expo/ui';
import { useCallback } from 'react';

function formatPhone(input: string) {
  'worklet';
  const digits = input.replace(/\D/g, '').slice(0, 10);
  if (digits.length <= 3) return digits;
  if (digits.length <= 6) return `(${digits.slice(0, 3)}) ${digits.slice(3)}`;
  return `(${digits.slice(0, 3)}) ${digits.slice(3, 6)}-${digits.slice(6)}`;
}

export default function PhoneMaskExample() {
  const phone = useNativeState('');
  const selection = useNativeState({ start: 0, end: 0 });

  const handleChangeText = useCallback(
    (value: string) => {
      'worklet';
      const formatted = formatPhone(value);
      if (formatted !== value) {
        phone.value = formatted;
        // Snaps to end for demo. Real masks need smarter cursor handling.
        selection.value = { start: formatted.length, end: formatted.length };
      }
    },
    [phone, selection]
  );

  return (
    <Host matchContents={{ vertical: true }}>
      <TextInput
        value={phone}
        selection={selection}
        keyboardType="phone-pad"
        placeholder="(555) 123-4567"
        onChangeText={handleChangeText}
      />
    </Host>
  );
}
```

## Unsupported React Native props

Some React Native `TextInput` props are not supported, because Compose's `TextField` or SwiftUI's `TextField` does not expose an equivalent, or because the prop is replaced by a different mechanism. See the [API](/versions/latest/sdk/ui/universal/textinput.md#api) section below for the supported props. If a missing prop blocks your use case, [open an issue](https://github.com/expo/expo/issues/new/choose) so it can be prioritized.

## API

```tsx
import { TextInput, useNativeState } from '@expo/ui';
```

## Component

### `TextInput`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TextInputProps](#textinputprops)\>

Props for the `TextInput` component.

TextInputProps

### `autoCapitalize`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `string` • Default: `'sentences'`

Controls automatic capitalization of input.

Acceptable values are: `'none'` | `'words'` | `'sentences'` | `'characters'`

### `autoComplete`

Supported platforms: Android, iOS, Web.

Optional • Type: [AutoComplete](#autocomplete)

Autofill hint. iOS maps to `textContentType`; Android maps to Compose's `Modifier.semantics { contentType = ... }`.

### `autoCorrect`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `true`

If false, disables autocorrect / spellcheck suggestions.

### `autoFocus`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

If true, focuses the input on mount.

### `caretHidden`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

If true, the cursor is hidden.

On iOS, this is implemented via `tint('transparent')`, which also makes the selection highlight invisible. If you set both `caretHidden` and `selectionColor`, the caret-hide wins on iOS.

### `cursorColor`

Supported platforms: Android, iOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Color of the text cursor.

### `defaultValue`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Initial text shown when the input mounts and `value` is not provided. Ignored once the user starts typing or if `value` is set.

### `editable`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `true`

If false, the input cannot be edited. Selection is still allowed so the user can copy text out of the field.

### `enterKeyHint`

Supported platforms: Android, iOS, Web.

Optional • Type: [EnterKeyHint](#enterkeyhint)

HTML-style hint for the keyboard return key. Maps to `returnKeyType`. When both are set, `returnKeyType` wins.

### `inputMode`

Supported platforms: Android, iOS, Web.

Optional • Type: [InputMode](#inputmode)

HTML-style hint for the keyboard variant. Maps to `keyboardType`. When both are set, `keyboardType` wins.

### `keyboardType`

Supported platforms: Android, iOS, Web.

Optional • Type: [KeyboardTypeOptions](https://reactnative.dev/docs/textinput#keyboardtype) • Default: `'default'`

Determines which keyboard variant is shown.

Lacking native support:

-   iOS: `'visible-password'` falls back to the default keyboard.
-   Android: iOS-specific values (`'ascii-capable'`, `'numbers-and-punctuation'`, `'name-phone-pad'`, `'twitter'`, `'web-search'`) fall back to the text keyboard.

### `maxLength`

Supported platforms: Android, iOS, Web.

Optional • Type: `number`

Maximum number of characters allowed.

### `modifiers`

Supported platforms: Android, iOS.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. Modifiers from the wrong platform are ignored at runtime.

### `multiline`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

If true, the field accepts multiple lines of input and grows vertically as the user types.

### `numberOfLines`

Supported platforms: Android, iOS, Web.

Optional • Type: `number`

Number of lines the field reserves when `multiline` is true. Forces a fixed visible height of that many lines.

Lacking native support:

-   iOS: requires iOS 16+; below that, the field grows naturally.

### `onBlur`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the field loses focus.

### `onChangeText`

Supported platforms: Android, iOS, Web.

Optional • Type: `(text: string) => void`

Called every time the text value changes. Receives the new string.

### `onContentSizeChange`

Supported platforms: Android, iOS, Web.

Optional • Type: `(size: { height: number, width: number }) => void`

Called when the rendered size of the input changes. Sizes in points/dp.

Unlike RN's `onContentSizeChange`, this dispatches the _view_'s outer geometry, including any padding/border applied via `style` or modifiers. If you use this for autogrow, account for that.

### `onFocus`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the field gains focus.

### `onSelectionChange`

Supported platforms: Android, iOS, Web.

Optional • Type: `(selection: { end: number, start: number }) => void`

Called when the text selection range changes.

### `onSubmitEditing`

Supported platforms: Android, iOS, Web.

Optional • Type: `(text: string) => void`

Called when the user taps the keyboard return key. Receives the current text in the input.

### `placeholder`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Placeholder text shown when the field is empty.

### `placeholderTextColor`

Supported platforms: Android, iOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Color of the placeholder text.

### `readOnly`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

Alias for `editable={false}`. When both are set, `editable` wins.

### `ref`

Supported platforms: Android, iOS, Web.

Optional • Type: Ref<[TextInputRef](#textinputref)\>

Ref exposing imperative methods (`focus`, `blur`, `clear`).

### `returnKeyType`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReturnKeyTypeOptions](https://reactnative.dev/docs/textinput#returnkeytype)

Determines the label of the keyboard return key.

Lacking native support:

-   iOS: `'emergency-call'` falls back to the default Return key.
-   Android: `'join'`, `'route'`, `'emergency-call'` fall back to the default action.

### `rows`

Supported platforms: Android, iOS, Web.

Optional • Type: `number`

HTML-style alias for `numberOfLines`. When both are set, `numberOfLines` wins.

### `secureTextEntry`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

If true, the input obscures its text — used for password fields.

-   iOS: backed by SwiftUI's `SecureField`. The following props are no-ops in this mode: `selection`, `selectTextOnFocus`, `onSelectionChange`, `multiline`, `numberOfLines`.
-   Android: backed by Compose's `PasswordVisualTransformation`.

### `selection`

Supported platforms: iOS 18.0+ — pre-ios 18 the prop is ignored..

Optional • Type: [ObservableState](#observablestate)<{ end: number, start: number }\>

Observable state the field writes the current selection to. Create with `useNativeState({ start: 0, end: 0 })`. Use `ref.setSelection(start, end)` to set selection programmatically.

### `selectionColor`

Supported platforms: Android, iOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Color of the selected text highlight. On iOS this also tints the cursor (UIKit's `tintColor` covers both); pass `cursorColor` only if you want different cursor color on Android.

### `selectionHandleColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Color of the selection drag handles.

### `selectTextOnFocus`

Supported platforms: iOS 18.0+, android, web.

Optional • Type: `boolean` • Default: `false`

If true, all text is selected when the field gains focus. Implemented via `setSelection(0, length)` on focus, so if you also pass `selection`, its value is overwritten on every focus.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Box-level style — sizing, padding, background, border, opacity.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `textAlign`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `string` • Default: `'auto'`

Horizontal alignment of the text content.

Lacking native support:

-   iOS: `'justify'` is not supported by SwiftUI's `TextField` and falls back to the default alignment.

Acceptable values are: `'auto'` | `'center'` | `'left'` | `'right'` | `'justify'`

### `textStyle`

Supported platforms: Android, iOS, Web.

Optional • Type: `{ color: string, fontFamily: string, fontSize: number, fontWeight: 'normal' | 'bold' | '100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900', letterSpacing: number, lineHeight: number, textAlign: 'center' | 'left' | 'right' }`

Text-level style — font, color, alignment, spacing.

> **Deprecated:** The Android `TextInput` renders an unstyled `BasicTextField` that has no underline indicator, so this has no effect. To draw your own border, pass it through `style` or `modifiers`.

### `underlineColorAndroid`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Color of the underline indicator on Android.

### `value`

Supported platforms: Android, iOS, Web.

Optional • Type: [ObservableState](#observablestate)<string\>

An observable state holding the current text. Create one with `useNativeState('initial value')` from `@expo/ui`. Omit to let the field manage its own internal state.

## Types

### `ObservableState`

Supported platforms: Android, iOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| value | `T` | - |

### `TextInputRef`

Supported platforms: Android, iOS, Web.

Imperative methods exposed via the `TextInput` ref.

| Property | Type | Description |
| --- | --- | --- |
| blur | `() => void` | Programmatically blur the input. |
| clear | `() => void` | Clear the current text. |
| focus | `() => void` | Programmatically focus the input. |
| isFocused | `() => boolean` | Returns whether the input currently has focus. |
| setSelection | (start: number, end: number) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Supported platforms: iOS 18.0+. Programmatically set the selection range. |
