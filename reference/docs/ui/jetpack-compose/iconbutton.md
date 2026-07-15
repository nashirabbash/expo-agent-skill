---
title: "IconButton"
description: "Jetpack Compose IconButton components for displaying native Material3 icon buttons."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/iconbutton.md"
scraped_at: "2026-07-15T09:00:50.496459"
---

---
title: IconButton
description: Jetpack Compose IconButton components for displaying native Material3 icon buttons.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# IconButton

Jetpack Compose IconButton components for displaying native Material3 icon buttons.
Android, Included in Expo Go

Expo UI provides four icon button components that match the official Jetpack Compose [IconButton API](https://developer.android.com/develop/ui/compose/components/icon-button): `IconButton`, `FilledIconButton`, `FilledTonalIconButton`, and `OutlinedIconButton`. All variants share the same props and accept composable children for content.

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

### Basic icon button

A standard icon button with no background, typically used for toolbar actions.

```tsx
import { Host, IconButton, Icon } from '@expo/ui/jetpack-compose';

export default function BasicIconButtonExample() {
  return (
    <Host matchContents>
      <IconButton onClick={() => alert('Pressed!')}>
        <Icon source={require('./assets/settings.xml')} size={24} />
      </IconButton>
    </Host>
  );
}
```

### Icon button variants

Use different icon button components to convey varying levels of emphasis.

```tsx
import {
  Host,
  IconButton,
  FilledIconButton,
  FilledTonalIconButton,
  OutlinedIconButton,
  Icon,
  Row,
} from '@expo/ui/jetpack-compose';

export default function IconButtonVariantsExample() {
  return (
    <Host matchContents>
      <Row horizontalArrangement={{ spacedBy: 8 }}>
        <IconButton onClick={() => {}}>
          <Icon source={require('./assets/star.xml')} size={24} />
        </IconButton>
        <FilledIconButton onClick={() => {}}>
          <Icon source={require('./assets/star.xml')} size={24} />
        </FilledIconButton>
        <FilledTonalIconButton onClick={() => {}}>
          <Icon source={require('./assets/star.xml')} size={24} />
        </FilledTonalIconButton>
        <OutlinedIconButton onClick={() => {}}>
          <Icon source={require('./assets/star.xml')} size={24} />
        </OutlinedIconButton>
      </Row>
    </Host>
  );
}
```

## API

```tsx
import {
  IconButton,
  FilledIconButton,
  FilledTonalIconButton,
  OutlinedIconButton,
} from '@expo/ui/jetpack-compose';
```

## Components

### `FilledIconButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconButtonProps](#iconbuttonprops)\>

A filled icon button with a solid background.

### `FilledTonalIconButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconButtonProps](#iconbuttonprops)\>

A filled tonal icon button with a muted background.

### `IconButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconButtonProps](#iconbuttonprops)\>

A standard icon button with no background.

IconButtonProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content to display inside the icon button.

### `colors`

Supported platforms: Android.

Optional • Type: [IconButtonColors](#iconbuttoncolors)

Colors for icon button elements.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the icon button is enabled for user interaction.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the icon button is clicked.

### `shape`

Supported platforms: Android.

Optional • Type: [ShapeJSXElement](/versions/v57.0.0/sdk/ui/jetpack-compose/shape.md#shapejsxelement)

The shape of the icon button.

### `OutlinedIconButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconButtonProps](#iconbuttonprops)\>

An outlined icon button with a border and no fill.

## Types

### `IconButtonColors`

Supported platforms: Android.

Colors for icon button elements.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| contentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
