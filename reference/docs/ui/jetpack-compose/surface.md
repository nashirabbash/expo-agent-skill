---
title: "Surface"
description: "A Jetpack Compose Surface component for styled content containers."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/surface.md"
scraped_at: "2026-07-15T09:00:33.787380"
---

---
title: Surface
description: A Jetpack Compose Surface component for styled content containers.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Surface

A Jetpack Compose Surface component for styled content containers.
Android, Included in Expo Go

Expo UI Surface matches the official Jetpack Compose [Surface](https://developer.android.com/develop/ui/compose/designsystems/material3) API and provides a container that applies Material Design surface styling including color, elevation, and content color.

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

### Basic surface

```tsx
import { Host, Surface, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function BasicSurfaceExample() {
  return (
    <Host matchContents>
      <Surface modifiers={[paddingAll(16)]}>
        <Text>Content on a surface</Text>
      </Surface>
    </Host>
  );
}
```

### Surface with elevation

Use `tonalElevation` and `shadowElevation` to control the visual depth of the surface.

```tsx
import { Host, Surface, Column, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function SurfaceElevationExample() {
  return (
    <Host matchContents>
      <Column modifiers={[paddingAll(16)]}>
        <Surface tonalElevation={1} shadowElevation={2} modifiers={[paddingAll(16)]}>
          <Text>Low elevation</Text>
        </Surface>
        <Surface tonalElevation={4} shadowElevation={8} modifiers={[paddingAll(16)]}>
          <Text>High elevation</Text>
        </Surface>
      </Column>
    </Host>
  );
}
```

### Surface with custom colors

Use the `color` and `contentColor` props to override the default Material theme colors.

```tsx
import { Host, Surface, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function SurfaceCustomColorsExample() {
  return (
    <Host matchContents>
      <Surface
        color="#1E3A5F"
        contentColor="#FFFFFF"
        tonalElevation={2}
        modifiers={[paddingAll(16)]}>
        <Text color="#FFFFFF">Custom colored surface</Text>
      </Surface>
    </Host>
  );
}
```

### Surface with shape and border

Use the `shape` prop to clip content and `border` to draw a stroke around the surface.

```tsx
import { Host, Surface, Shape, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function SurfaceShapeBorderExample() {
  return (
    <Host matchContents>
      <Surface
        shape={Shape.RoundedCorner({
          cornerRadii: { topStart: 16, topEnd: 16, bottomStart: 16, bottomEnd: 16 },
        })}
        border={{ width: 2, color: '#6200EE' }}
        modifiers={[paddingAll(16)]}>
        <Text>Rounded surface with border</Text>
      </Surface>
    </Host>
  );
}
```

## API

```tsx
import { Surface } from '@expo/ui/jetpack-compose';
```

## Component

### `Surface`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SurfaceProps](#surfaceprops)\>

A Material Design surface container. Surface is responsible for:

-   Clipping content to the shape
-   Applying background color based on tonal elevation
-   Providing content color to its children

SurfaceProps

### `border`

Supported platforms: Android.

Optional • Type: [SurfaceBorder](#surfaceborder)

Border stroke drawn around the surface.

### `checked`

Supported platforms: Android.

Optional • Type: `boolean`

Whether the surface is in a checked (toggled on) state. When provided together with `onCheckedChange`, the surface becomes a toggleable surface.

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to display inside the surface.

### `color`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The background color of the surface. Defaults to `MaterialTheme.colorScheme.surface`.

### `contentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the content inside the surface. Defaults to `contentColorFor(color)`.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the surface is enabled and responds to user interaction.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onCheckedChange`

Supported platforms: Android.

Optional • Type: `(checked: boolean) => void`

Called when the checked state of a toggleable surface changes. Providing this callback together with `checked` enables the toggleable variant.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Called when the surface is clicked. Providing this callback makes the surface clickable. When combined with `selected`, the surface becomes a selectable variant.

### `selected`

Supported platforms: Android.

Optional • Type: `boolean`

Whether the surface is in a selected state. When provided together with `onClick`, the surface becomes a selectable surface that visually reflects its selection state.

### `shadowElevation`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

The shadow elevation of the surface. Value in dp.

### `shape`

Supported platforms: Android.

Optional • Type: [ShapeJSXElement](/versions/v57.0.0/sdk/ui/jetpack-compose/shape.md#shapejsxelement)

Shape configuration for clipping the surface.

### `tonalElevation`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

The tonal elevation of the surface, which affects its background color based on the color scheme. Value in dp.

## Types

### `SurfaceBorder`

Supported platforms: Android.

Border stroke configuration.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Border color. Default: `MaterialTheme.colorScheme.outline` |
| width(optional) | `number` | Border width in dp. Default: `1` |
