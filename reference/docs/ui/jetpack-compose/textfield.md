---
title: "TextField"
description: "Jetpack Compose TextField components for native Material3 text input."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/textfield.md"
scraped_at: "2026-07-15T09:00:28.020951"
---

---
title: TextField
description: Jetpack Compose TextField components for native Material3 text input.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# TextField

Jetpack Compose TextField components for native Material3 text input.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`TextInput`](/versions/latest/sdk/ui/universal/textinput.md) — it renders the appropriate native component per platform.

Expo UI provides three text field components that match the official Jetpack Compose [TextField API](https://developer.android.com/develop/ui/compose/text/user-input): `TextField` (filled), `OutlinedTextField` (outlined border), and `BasicTextField` (unstyled). The Material variants `TextField` and `OutlinedTextField` share the same props and support composable slot children for label, placeholder, icons, prefix, suffix, and supporting text. `BasicTextField` has no Material chrome, so you supply your own decoration.

| Type | Appearance | Purpose |
| --- | --- | --- |
| Filled | Solid background with a bottom indicator line. | Default text input style following Material3 design. Use for most forms and input fields. |
| Outlined | Transparent background with a border outline. | Alternative style that provides a distinct visual boundary. Use when filled fields blend into the background. |
| Basic | No container, indicator, or padding. Just the editable text. | Fully custom-styled inputs. Style it yourself and add decoration through `DecorationBox`. |

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

Bind a [`useNativeState`](/versions/latest/sdk/ui/jetpack-compose/usenativestate.md) observable to `value`. The field tracks the user's input on its own, and you read the current value from `text.value`. The filled style shown here is the default Material3 text input.

```tsx
import { Host, TextField, Text, useNativeState } from '@expo/ui/jetpack-compose';

export default function UncontrolledTextFieldExample() {
  const text = useNativeState('');

  return (
    <Host matchContents>
      <TextField value={text}>
        <TextField.Label>
          <Text>Username</Text>
        </TextField.Label>
      </TextField>
    </Host>
  );
}
```

### Controlled text field

Pass a [`useNativeState`](/versions/latest/sdk/ui/jetpack-compose/usenativestate.md) observable as `value` and an `onValueChange` worklet to transform or validate input before writing it back. The example below uppercases the text as it is typed.

> **Note:** Worklets require installing [`react-native-worklets`](https://docs.swmansion.com/react-native-worklets/).

```tsx
import { Host, TextField, Text, useNativeState } from '@expo/ui/jetpack-compose';
import { useCallback } from 'react';

export default function ControlledTextFieldExample() {
  const text = useNativeState('');

  const handleValueChange = useCallback(
    (value: string) => {
      'worklet';
      text.value = value.toUpperCase();
    },
    [text]
  );

  return (
    <Host matchContents>
      <TextField value={text} onValueChange={handleValueChange}>
        <TextField.Label>
          <Text>Name</Text>
        </TextField.Label>
      </TextField>
    </Host>
  );
}
```

### Outlined text field

Use `OutlinedTextField` for a text field with a border outline instead of a filled background.

```tsx
import { Host, OutlinedTextField, Text, useNativeState } from '@expo/ui/jetpack-compose';

export default function OutlinedTextFieldExample() {
  const text = useNativeState('');

  return (
    <Host matchContents>
      <OutlinedTextField value={text}>
        <OutlinedTextField.Label>
          <Text>Email</Text>
        </OutlinedTextField.Label>
        <OutlinedTextField.Placeholder>
          <Text>you@example.com</Text>
        </OutlinedTextField.Placeholder>
      </OutlinedTextField>
    </Host>
  );
}
```

### Basic text field

`BasicTextField` is the unstyled Compose primitive, with no container, indicator, or padding. Style it yourself with [modifiers](/versions/latest/sdk/ui/jetpack-compose/modifiers.md) and supply decoration through `DecorationBox`, placing `InnerTextField` where the editable text should render. Wrap placeholder content in `Placeholder` to have it shown only while the field is empty, toggled natively from the field's text.

```tsx
import { Host, BasicTextField, Box, Text, useNativeState } from '@expo/ui/jetpack-compose';
import {
  background,
  clip,
  fillMaxWidth,
  padding,
  Shapes,
} from '@expo/ui/jetpack-compose/modifiers';

export default function BasicTextFieldExample() {
  const value = useNativeState('');

  return (
    <Host matchContents>
      <BasicTextField
        cursorColor="#7c3aed"
        value={value}
        modifiers={[
          fillMaxWidth(),
          clip(Shapes.RoundedCorner(12)),
          background('#f3f4f6'),
          padding(12, 10, 12, 10),
        ]}>
        <BasicTextField.DecorationBox>
          <Box>
            <BasicTextField.Placeholder>
              <Text color="#9ca3af">Search…</Text>
            </BasicTextField.Placeholder>
            <BasicTextField.InnerTextField />
          </Box>
        </BasicTextField.DecorationBox>
      </BasicTextField>
    </Host>
  );
}
```

### Slots

Both `TextField` and `OutlinedTextField` support 7 composable slots that match the Compose API: `Label`, `Placeholder`, `LeadingIcon`, `TrailingIcon`, `Prefix`, `Suffix`, and `SupportingText`.

```tsx
import { Host, TextField, Text, useNativeState } from '@expo/ui/jetpack-compose';

export default function TextFieldSlotsExample() {
  const text = useNativeState('');

  return (
    <Host matchContents>
      <TextField value={text}>
        <TextField.Label>
          <Text>Price</Text>
        </TextField.Label>
        <TextField.Placeholder>
          <Text>0.00</Text>
        </TextField.Placeholder>
        <TextField.LeadingIcon>
          <Text>💰</Text>
        </TextField.LeadingIcon>
        <TextField.Prefix>
          <Text>$</Text>
        </TextField.Prefix>
        <TextField.Suffix>
          <Text>USD</Text>
        </TextField.Suffix>
        <TextField.SupportingText>
          <Text>Enter the amount</Text>
        </TextField.SupportingText>
      </TextField>
    </Host>
  );
}
```

### Keyboard options

Use the `keyboardOptions` prop to configure the keyboard type, capitalization, auto-correct, and IME action.

```tsx
import { Host, TextField, Text, useNativeState } from '@expo/ui/jetpack-compose';

export default function KeyboardOptionsExample() {
  const text = useNativeState('');

  return (
    <Host matchContents>
      <TextField
        value={text}
        singleLine
        keyboardOptions={{
          keyboardType: 'email',
          capitalization: 'none',
          autoCorrectEnabled: false,
          imeAction: 'done',
        }}>
        <TextField.Label>
          <Text>Email</Text>
        </TextField.Label>
      </TextField>
    </Host>
  );
}
```

### Keyboard actions

Use the `keyboardActions` prop to handle IME action button presses. The triggered callback depends on the `imeAction` set in `keyboardOptions`. Each callback receives the current text value.

```tsx
import { Host, TextField, Text, useNativeState } from '@expo/ui/jetpack-compose';

export default function KeyboardActionsExample() {
  const text = useNativeState('');

  return (
    <Host matchContents>
      <TextField
        value={text}
        singleLine
        keyboardOptions={{ imeAction: 'search' }}
        keyboardActions={{
          onSearch: value => console.log('Searched:', value),
        }}>
        <TextField.Label>
          <Text>Search</Text>
        </TextField.Label>
      </TextField>
    </Host>
  );
}
```

### Imperative ref

Use a ref to imperatively set text, clear the field, change the selection, or move focus.

```tsx
import { useRef } from 'react';
import {
  Host,
  TextField,
  TextFieldRef,
  Button,
  Row,
  Text,
  Column,
  useNativeState,
} from '@expo/ui/jetpack-compose';
import { padding } from '@expo/ui/jetpack-compose/modifiers';

export default function ImperativeRefExample() {
  const ref = useRef<TextFieldRef>(null);
  const text = useNativeState('');

  return (
    <Host matchContents>
      <Column>
        <TextField ref={ref} value={text} singleLine>
          <TextField.Label>
            <Text>Name</Text>
          </TextField.Label>
        </TextField>
        <Row horizontalArrangement={{ spacedBy: 8 }} modifiers={[padding(8, 0, 0, 0)]}>
          <Button onClick={() => ref.current?.setText('Hello world')}>
            <Text>Set text</Text>
          </Button>
          <Button onClick={() => ref.current?.clear()}>
            <Text>Clear</Text>
          </Button>
          <Button onClick={() => ref.current?.setSelection(0, 5)}>
            <Text>Select first word</Text>
          </Button>
        </Row>
        <Row horizontalArrangement={{ spacedBy: 8 }} modifiers={[padding(8, 0, 0, 0)]}>
          <Button onClick={() => ref.current?.focus()}>
            <Text>Focus</Text>
          </Button>
          <Button onClick={() => ref.current?.blur()}>
            <Text>Blur</Text>
          </Button>
        </Row>
      </Column>
    </Host>
  );
}
```

### Worklet text masking

When `onValueChange` is marked with the `'worklet'` directive, it runs synchronously on the UI thread, so writes to [`useNativeState`](/versions/latest/sdk/ui/jetpack-compose/usenativestate.md) observables inside the callback take effect before the next frame. There is no flicker between the typed text and the masked text. The example below masks a phone number as the user types and writes both `value` and `selection` from the worklet to keep the cursor at the end of the formatted value.

> **Note:** Worklets require installing [`react-native-worklets`](https://docs.swmansion.com/react-native-worklets/).

```tsx
import { Host, TextField, Text, useNativeState } from '@expo/ui/jetpack-compose';
import { fillMaxWidth } from '@expo/ui/jetpack-compose/modifiers';
import { useEffectEvent } from 'react';

export default function WorkletPhoneMaskExample() {
  const phone = useNativeState('');
  const selection = useNativeState({ start: 0, end: 0 });

  const handleValueChange = useEffectEvent((v: string) => {
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
        value={phone}
        selection={selection}
        keyboardOptions={{ keyboardType: 'phone' }}
        modifiers={[fillMaxWidth()]}
        onValueChange={handleValueChange}>
        <TextField.Placeholder>
          <Text>(555) 123-4567</Text>
        </TextField.Placeholder>
      </TextField>
    </Host>
  );
}
```

## API

```tsx
import { TextField, OutlinedTextField, BasicTextField } from '@expo/ui/jetpack-compose';
```

## Components

### `BasicTextField`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BasicTextFieldProps](#basictextfieldprops)\>

A bare, unstyled Compose `BasicTextField` with no Material decoration.

Props for `BasicTextField`. Mirrors Compose's `BasicTextField`: a bare, unstyled text field with no Material chrome (no container, indicator, or built-in padding). Shares [`CommonTextFieldProperties`](#commontextfieldproperties) with `TextField` and `OutlinedTextField`; use `BasicTextField.DecorationBox` to add your own decoration.

BasicTextFieldProps

### `cursorColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Color of the text cursor. Maps to Compose's `cursorBrush` via `SolidColor(color)`. Defaults to the theme's primary color (`MaterialTheme.colorScheme.primary`) so it stays visible in light and dark.

#### Inherited Props

-   [CommonTextFieldProperties](#commontextfieldproperties)

### `OutlinedTextField`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[OutlinedTextFieldProps](#outlinedtextfieldprops)\>

A Material3 `OutlinedTextField` with a transparent background and border outline.

Props shared by every Compose text field variant — `TextField`, `OutlinedTextField`, and `BasicTextField`. The Material variants add their own decoration props (`isError`, `shape`, `colors`, slot children); `BasicTextField` adds `cursorColor`.

OutlinedTextFieldProps

### `colors`

Supported platforms: Android.

Optional • Type: [TextFieldColors](#textfieldcolors)

### `isError`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

### `shape`

Supported platforms: Android.

Optional • Type: [ShapeJSXElement](/versions/v57.0.0/sdk/ui/jetpack-compose/shape.md#shapejsxelement)

Shape used for the field's container outline/fill. Use the helpers from `Shape` (for example, `<Shape.Pill />` or `<Shape.RoundedCorner cornerRadii={...} />`). Defaults to the Material `OutlinedTextFieldDefaults.shape`/`TextFieldDefaults.shape`.

#### Inherited Props

-   [CommonTextFieldProperties](#commontextfieldproperties)

### `TextField`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TextFieldProps](#textfieldprops)\>

A Material3 `TextField`.

Props shared by every Compose text field variant — `TextField`, `OutlinedTextField`, and `BasicTextField`. The Material variants add their own decoration props (`isError`, `shape`, `colors`, slot children); `BasicTextField` adds `cursorColor`.

TextFieldProps

### `colors`

Supported platforms: Android.

Optional • Type: [TextFieldColors](#textfieldcolors)

### `isError`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

### `shape`

Supported platforms: Android.

Optional • Type: [ShapeJSXElement](/versions/v57.0.0/sdk/ui/jetpack-compose/shape.md#shapejsxelement)

Shape used for the field's container outline/fill. Use the helpers from `Shape` (for example, `<Shape.Pill />` or `<Shape.RoundedCorner cornerRadii={...} />`). Defaults to the Material `OutlinedTextFieldDefaults.shape`/`TextFieldDefaults.shape`.

#### Inherited Props

-   [CommonTextFieldProperties](#commontextfieldproperties)

## Types

### `BasicTextFieldRef`

Supported platforms: Android.

Type: [TextFieldRef](#textfieldref)

Imperative methods for `BasicTextField`. Identical to [`TextFieldRef`](#textfieldref).

### `CommonTextFieldProperties`

Supported platforms: Android.

Props shared by every Compose text field variant — `TextField`, `OutlinedTextField`, and `BasicTextField`. The Material variants add their own decoration props (`isError`, `shape`, `colors`, slot children); `BasicTextField` adds `cursorColor`.

| Property | Type | Description |
| --- | --- | --- |
| autoFocus(optional) | `boolean` | If true, the text field will be focused automatically when mounted. Default: `false` |
| children(optional) | [ReactNode](https://reactnative.dev/docs/react-node) | Slot children that configure the field's decoration. |
| enabled(optional) | `boolean` | Default: `true` |
| keyboardActions(optional) | [TextFieldKeyboardActions](#textfieldkeyboardactions) | - |
| keyboardOptions(optional) | [TextFieldKeyboardOptions](#textfieldkeyboardoptions) | - |
| maxLength(optional) | `number` | Maximum number of characters allowed. Truncates natively as the user types. |
| maxLines(optional) | `number` | - |
| minLines(optional) | `number` | - |
| modifiers(optional) | `ModifierConfig[]` | - |
| onFocusChanged(optional) | `(focused: boolean) => void` | A callback triggered when the field gains or loses focus. |
| onSelectionChange(optional) | `(selection: { end: number, start: number }) => void` | Called when the selection range changes. |
| onValueChange(optional) | `(value: string) => void` | Fires whenever the text value changes. If marked with the `'worklet'` directive, runs synchronously on the UI thread; otherwise delivered asynchronously as a regular JS event. Use `onSelectionChange` (or read the `selection` observable) to react to selection-only changes. |
| readOnly(optional) | `boolean` | Default: `false` |
| ref(optional) | Ref<[TextFieldRef](#textfieldref)\> | - |
| selection(optional) | [ObservableState](#observablestate)<{ end: number, start: number }\> | Observable state holding the current selection range. Create with `useNativeState({ start: 0, end: 0 })`. The field writes user-driven changes back to it, and writes from JS (or a worklet) update the cursor/selection in the field. Use `ref.setSelection(start, end)` for imperative one-shot updates. |
| singleLine(optional) | `boolean` | Default: `false` |
| textSelectionColors(optional) | { backgroundColor: [ColorValue](https://reactnative.dev/docs/colors), handleColor: [ColorValue](https://reactnative.dev/docs/colors) } | Selection-related colors. Maps to Compose's `TextSelectionColors` via `LocalTextSelectionColors`. `handleColor` controls the drag handles (and the caret's drag handle); `backgroundColor` is the highlighted-text background (typically the same tint at lower alpha so the underlying text stays readable). Independent of `cursorColor`, which tints the caret line. |
| textStyle(optional) | [TextFieldTextStyle](#textfieldtextstyle) | Text styling for the field's content. Maps to Compose's `TextStyle`. |
| value(optional) | [ObservableState](#observablestate)<string\> | An observable state that holds the current text value. Create one with `useNativeState('initial text')`. If omitted, the field manages its own internal state. |
| visualTransformation(optional) | `'password' | 'none'` | Display-time text transformation. `'password'` masks every character; `'none'` (default) leaves the buffer as-is. |

### `ObservableState`

Supported platforms: Android.

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

### `TextFieldCapitalization`

Supported platforms: Android.

Literal Type: `string`

Acceptable values are: `'none'` | `'characters'` | `'words'` | `'sentences'`

### `TextFieldColors`

Supported platforms: Android.

Colors for `TextField` and `OutlinedTextField`. Maps to `TextFieldColors` in Compose, shared by both variants.

| Property | Type | Description |
| --- | --- | --- |
| cursorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledIndicatorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledLabelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledLeadingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledPlaceholderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledPrefixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledSuffixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledSupportingTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledTrailingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorCursorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorIndicatorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorLabelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorLeadingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorPlaceholderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorPrefixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorSuffixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorSupportingTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| errorTrailingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedIndicatorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedLabelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedLeadingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedPlaceholderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedPrefixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedSuffixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedSupportingTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| focusedTrailingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedIndicatorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedLabelColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedLeadingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedPlaceholderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedPrefixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedSuffixColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedSupportingTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unfocusedTrailingIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `TextFieldImeAction`

Supported platforms: Android.

Literal Type: `string`

Acceptable values are: `'default'` | `'none'` | `'go'` | `'search'` | `'send'` | `'previous'` | `'next'` | `'done'`

### `TextFieldKeyboardActions`

Supported platforms: Android.

Keyboard actions matching Compose `KeyboardActions`. The triggered callback depends on the `imeAction` in `keyboardOptions`.

| Property | Type | Description |
| --- | --- | --- |
| onDone(optional) | `(value: string) => void` | - |
| onGo(optional) | `(value: string) => void` | - |
| onNext(optional) | `(value: string) => void` | - |
| onPrevious(optional) | `(value: string) => void` | - |
| onSearch(optional) | `(value: string) => void` | - |
| onSend(optional) | `(value: string) => void` | - |

### `TextFieldKeyboardOptions`

Supported platforms: Android.

Keyboard options matching Compose `KeyboardOptions`.

| Property | Type | Description |
| --- | --- | --- |
| autoCorrectEnabled(optional) | `boolean` | Default: `true` |
| capitalization(optional) | [TextFieldCapitalization](#textfieldcapitalization) | Default: `'none'` |
| imeAction(optional) | [TextFieldImeAction](#textfieldimeaction) | Default: `'default'` |
| keyboardType(optional) | [TextFieldKeyboardType](#textfieldkeyboardtype) | Default: `'text'` |

### `TextFieldKeyboardType`

Supported platforms: Android.

Literal Type: `string`

Acceptable values are: `'text'` | `'number'` | `'email'` | `'phone'` | `'decimal'` | `'password'` | `'ascii'` | `'uri'` | `'numberPassword'`

### `TextFieldRef`

Supported platforms: Android.

Can be used for imperatively focusing and setting text/selection on the `TextField`, `OutlinedTextField`, and `BasicTextField` components.

| Property | Type | Description |
| --- | --- | --- |
| blur | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |
| clear | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Clear the current text. |
| focus | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |
| setSelection | (start: number, end: number) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Programmatically set the selection range. |
| setText | (newText: string) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | - |

### `TextFieldTextStyle`

Supported platforms: Android.

Text styling for a text field's content. Maps to Compose's `TextStyle`. Shared by `TextField`, `OutlinedTextField`, and `BasicTextField`.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| fontFamily(optional) | `string` | - |
| fontSize(optional) | `number` | - |
| fontWeight(optional) | `'100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900' | 'normal' | 'bold'` | - |
| letterSpacing(optional) | `number` | - |
| lineHeight(optional) | `number` | - |
| textAlign(optional) | `'left' | 'right' | 'center' | 'justify'` | - |
