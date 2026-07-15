---
title: "HorizontalFloatingToolbar"
description: "A Jetpack Compose HorizontalFloatingToolbar component for displaying a floating action bar."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/horizontalfloatingtoolbar.md"
scraped_at: "2026-07-15T09:00:48.978342"
---

---
title: HorizontalFloatingToolbar
description: A Jetpack Compose HorizontalFloatingToolbar component for displaying a floating action bar.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# HorizontalFloatingToolbar

A Jetpack Compose HorizontalFloatingToolbar component for displaying a floating action bar.
Android, Included in Expo Go

Expo UI HorizontalFloatingToolbar wraps the official Jetpack Compose [`HorizontalFloatingToolbar`](https://kotlinlang.org/api/compose-multiplatform/material3/androidx.compose.material3/-horizontal-floating-toolbar.html) and displays a horizontal toolbar that floats above content, containing action buttons.

> **Note:** If you only need a single floating button, use [`FloatingActionButton`](/versions/latest/sdk/ui/jetpack-compose/floatingactionbutton.md) instead.

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

### Floating toolbar over scrollable content

Place the toolbar inside a `Box` with `floatingToolbarExitAlwaysScrollBehavior` to get scroll-driven hide/show behavior. Use `align('bottomCenter')` to position the toolbar at the bottom of the screen. The entire layout stays within the Compose layer — no React Native absolute positioning needed.

```tsx
import {
  Box,
  HorizontalFloatingToolbar,
  Host,
  Icon,
  IconButton,
  LazyColumn,
  ListItem,
} from '@expo/ui/jetpack-compose';
import { align, fillMaxSize, fillMaxWidth, offset } from '@expo/ui/jetpack-compose/modifiers';

export default function FloatingToolbarExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Box modifiers={[fillMaxSize()]} floatingToolbarExitAlwaysScrollBehavior="bottom">
        <LazyColumn modifiers={[fillMaxSize()]}>{/* ...list items... */}</LazyColumn>

        <HorizontalFloatingToolbar
          variant="vibrant"
          modifiers={[align('bottomCenter'), offset(0, -16)]}>
          <IconButton onClick={() => console.log('Edit pressed')}>
            <Icon source={require('./assets/edit.xml')} />
          </IconButton>
          <HorizontalFloatingToolbar.FloatingActionButton
            onClick={() => console.log('Add pressed')}>
            <Icon source={require('./assets/add.xml')} />
          </HorizontalFloatingToolbar.FloatingActionButton>
        </HorizontalFloatingToolbar>
      </Box>
    </Host>
  );
}
```

### Toolbar with FloatingActionButton

Use `IconButton` as direct children for toolbar items, and `HorizontalFloatingToolbar.FloatingActionButton` for the primary action.

```tsx
import { Host, HorizontalFloatingToolbar, IconButton, Icon } from '@expo/ui/jetpack-compose';

export default function ToolbarWithFABExample() {
  return (
    <Host matchContents>
      <HorizontalFloatingToolbar>
        <IconButton onClick={() => console.log('Edit pressed')}>
          <Icon source={require('./assets/edit.xml')} contentDescription="Edit" />
        </IconButton>
        <IconButton onClick={() => console.log('Share pressed')}>
          <Icon source={require('./assets/share.xml')} contentDescription="Share" />
        </IconButton>
        <HorizontalFloatingToolbar.FloatingActionButton onPress={() => console.log('Add pressed')}>
          <Icon source={require('./assets/add.xml')} contentDescription="Add" />
        </HorizontalFloatingToolbar.FloatingActionButton>
      </HorizontalFloatingToolbar>
    </Host>
  );
}
```

## API

```tsx
import { HorizontalFloatingToolbar } from '@expo/ui/jetpack-compose';
```

## Components

### `HorizontalFloatingToolbar`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[HorizontalFloatingToolbarProps](#horizontalfloatingtoolbarprops)\>

Renders a `HorizontalFloatingToolbar` component. A horizontal toolbar that floats above content, typically used for action buttons.

HorizontalFloatingToolbarProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The children of the component.

### `colors`

Supported platforms: Android.

Optional • Type: [HorizontalFloatingToolbarColors](#horizontalfloatingtoolbarcolors)

Per-slot color overrides. Any field set here replaces the corresponding color from the variant default; unset fields fall back to the variant.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `variant`

Supported platforms: Android.

Optional • Literal type: `string` • Default: `'standard'`

The variant of the horizontal floating toolbar.

Acceptable values are: `'standard'` | `'vibrant'`

### `HorizontalFloatingToolbarFloatingActionButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[HorizontalFloatingToolbarFloatingActionButtonProps](#horizontalfloatingtoolbarfloatingactionbuttonprops)\>

FloatingActionButton component for HorizontalFloatingToolbar. This component marks its children to be rendered in the FAB slot.

HorizontalFloatingToolbarFloatingActionButtonProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The children of the component.

### `onPress`

Supported platforms: Android.

Optional • Type: `() => void`

A callback that is called when the button is pressed.

## Types

### `HorizontalFloatingToolbarColors`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| fabContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Color of the floating action button container (background). |
| fabContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Color of the floating action button content (icon). |
| toolbarContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Color of the toolbar container (background). |
| toolbarContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Color of the toolbar content (icons/text). |
