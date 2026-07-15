---
title: "Picker"
description: "A single-selection input with menu and wheel appearances."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/picker.md"
scraped_at: "2026-07-15T09:01:35.420888"
---

---
title: Picker
description: A single-selection input with menu and wheel appearances.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Picker

A single-selection input with menu and wheel appearances.
Android, iOS, Web, Included in Expo Go

`Picker` is a single-selection input. You can use `<Picker.Item label value />` children to declare options so that the parent `Picker` reads them and renders a platform-appropriate dropdown or rotor.

The universal `Picker` is independent of [`@expo/ui/community/picker`](/versions/latest/sdk/ui/drop-in-replacements/picker.md), which remains a compat shim for `@react-native-picker/picker`. Prefer this universal `Picker` for new code unless you specifically need the RN-Picker API surface.

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

### Menu appearance (default)

```tsx
import { useState } from 'react';
import { Host, Row, Picker, Spacer, Text } from '@expo/ui';

const FLAVOURS = [
  { label: 'Vanilla', value: 'vanilla' },
  { label: 'Chocolate', value: 'chocolate' },
  { label: 'Strawberry', value: 'strawberry' },
];

export default function PickerMenuExample() {
  const [value, setValue] = useState('vanilla');

  return (
    <Host style={{ flex: 1 }}>
      <Row alignment="center" spacing={12} style={{ padding: 16 }}>
        <Text>Flavour:</Text>
        <Spacer flexible />
        <Picker selectedValue={value} onValueChange={setValue}>
          {FLAVOURS.map(f => (
            <Picker.Item key={f.value} label={f.label} value={f.value} />
          ))}
        </Picker>
      </Row>
    </Host>
  );
}
```

### Wheel appearance

`appearance="wheel"` renders an inline scrollable rotor on iOS. On Android and web, this falls back to the platform's default dropdown (Material 3 doesn't ship a wheel-style picker).

```tsx
import { useState } from 'react';
import { Host, Column, Picker } from '@expo/ui';

const FLAVOURS = [
  { label: 'Vanilla', value: 'vanilla' },
  { label: 'Chocolate', value: 'chocolate' },
  { label: 'Strawberry', value: 'strawberry' },
];

export default function PickerWheelExample() {
  const [value, setValue] = useState('chocolate');

  return (
    <Host style={{ flex: 1 }}>
      <Column spacing={8} style={{ padding: 16 }}>
        <Picker selectedValue={value} onValueChange={setValue} appearance="wheel">
          {FLAVOURS.map(f => (
            <Picker.Item key={f.value} label={f.label} value={f.value} />
          ))}
        </Picker>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { Picker } from '@expo/ui';
```

## Component

### `Picker`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[PickerProps](#pickerprops)<T\>\>

A single-selection input. Declare options via `<Picker.Item label value />` children.

Props for the [`Picker`](#picker) component, a single-selection input.

PickerProps

### `appearance`

Supported platforms: Android, iOS, Web.

Optional • Type: [PickerAppearance](#pickerappearance) • Default: `'menu'`

Visual appearance of the picker. See [`PickerAppearance`](#pickerappearance).

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

`<Picker.Item>` children that declare the available options.

### `enabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `true`

Whether the picker accepts input.

### `onValueChange`

Supported platforms: Android, iOS, Web.

Type: `(value: T) => void`

Called when the user selects an option.

### `selectedValue`

Supported platforms: Android, iOS, Web.

Type: `T`

The currently selected value. Must match the `value` of one of the `<Picker.Item>` children.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

## Interfaces

### `ExtractedPickerItem`

Supported platforms: Android, iOS, Web.

Internal: extracted item data from `<Picker.Item>` children.

| Property | Type | Description |
| --- | --- | --- |
| label | `string` | - |
| value | `T` | - |

## Types

### `PickerAppearance`

Supported platforms: Android, iOS, Web.

Literal Type: `string`

Visual appearance of the picker.

-   `'menu'` — Compact button that opens a popup/dropdown on tap. Cross-platform default.
-   `'wheel'` — Scrollable rotor UI that's always visible inline. iOS only; on Android and web this falls back to the platform's default dropdown.

Acceptable values are: `'wheel'` | `'menu'`

### `PickerItemValue`

Supported platforms: Android, iOS, Web.

Literal Type: `union`

The type of values a [`Picker.Item`](#pickeritem) can carry.

Acceptable values are: `string` | `number`
