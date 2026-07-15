---
title: "Button"
description: "A pressable button with multiple visual variants."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/button.md"
scraped_at: "2026-07-15T09:01:47.077766"
---

---
title: Button
description: A pressable button with multiple visual variants.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Button

A pressable button with multiple visual variants.
Android, iOS, Web, Included in Expo Go

A pressable button that renders consistently across Android, iOS, and web. Supports `filled`, `outlined`, and `text` visual variants.

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

### Basic button

```tsx
import { Host, Button } from '@expo/ui';

export default function BasicButtonExample() {
  return (
    <Host matchContents>
      <Button label="Press me" onPress={() => alert('Pressed!')} />
    </Host>
  );
}
```

### Variants

Pick a visual variant with the [`variant`](/versions/latest/sdk/ui/universal/button.md#variant) prop.

```tsx
import { Host, Column, Button } from '@expo/ui';

export default function ButtonVariantsExample() {
  return (
    <Host matchContents>
      <Column spacing={8}>
        <Button variant="filled" label="Filled" onPress={() => {}} />
        <Button variant="outlined" label="Outlined" onPress={() => {}} />
        <Button variant="text" label="Text" onPress={() => {}} />
      </Column>
    </Host>
  );
}
```

### Custom content

Pass [`children`](/versions/latest/sdk/ui/universal/button.md#children) for fully custom button contents. The [`label`](/versions/latest/sdk/ui/universal/button.md#label) prop is ignored when `children` is provided.

```tsx
import { Host, Button, Row, Icon, Text } from '@expo/ui';

export default function CustomButtonExample() {
  return (
    <Host matchContents>
      <Button onPress={() => {}}>
        <Row spacing={6} alignment="center">
          <Icon
            name={Icon.select({
              ios: 'star.fill',
              android: require('@expo/material-symbols/star.xml'),
            })}
            size={16}
            color="#FFFFFF"
          />
          <Text textStyle={{ color: '#FFFFFF' }}>Favorite</Text>
        </Row>
      </Button>
    </Host>
  );
}
```

### Disabled

```tsx
import { Host, Button } from '@expo/ui';

export default function DisabledButtonExample() {
  return (
    <Host matchContents>
      <Button label="Disabled" onPress={() => {}} disabled />
    </Host>
  );
}
```

## API

```tsx
import { Button } from '@expo/ui';
```

## Component

### `Button`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ButtonProps](#buttonprops)\>

A pressable button that supports multiple visual variants.

Props for the [`Button`](#button) component.

ButtonProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Custom content rendered inside the button. When provided, `label` is ignored.

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is disabled. Disabled components do not respond to user interaction.

### `hidden`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is hidden.

### `label`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Text label displayed inside the button. Ignored when `children` is provided.

### `modifiers`

Supported platforms: Android, iOS.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. A modifier supplied here replaces any modifier of the same type that the component derives from `style` or other props.

### `onAppear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component appears on screen.

### `onDisappear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is removed from screen.

### `onPress`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the button is pressed.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `variant`

Supported platforms: Android, iOS, Web.

Optional • Type: [ButtonVariant](#buttonvariant) • Default: `'filled'`

Visual variant of the button.

## Types

### `ButtonVariant`

Supported platforms: Android, iOS, Web.

Literal Type: `string`

Visual variant of a [`Button`](#button).

-   `'filled'` — solid background color (default).
-   `'outlined'` — transparent background with a border.
-   `'text'` — no background or border, text only.

Acceptable values are: `'filled'` | `'outlined'` | `'text'`
