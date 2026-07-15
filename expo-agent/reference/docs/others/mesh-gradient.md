---
title: "MeshGradient"
description: "A module that exposes MeshGradient view from SwiftUI to React Native."
source_url: "https://docs.expo.dev/versions/latest/sdk/mesh-gradient.md"
scraped_at: "2026-07-15T08:45:58.578771"
---

---
title: MeshGradient
description: A module that exposes MeshGradient view from SwiftUI to React Native.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-mesh-gradient'
packageName: 'expo-mesh-gradient'
iconUrl: '/static/images/packages/expo-mesh-gradient.png'
platforms: ['android', 'ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Expo MeshGradient

A module that exposes MeshGradient view from SwiftUI to React Native.
Android, iOS, tvOS, Included in Expo Go

## Installation

```sh
# npm
npx expo install expo-mesh-gradient

# yarn
yarn expo install expo-mesh-gradient

# pnpm
pnpm expo install expo-mesh-gradient

# bun
bun expo install expo-mesh-gradient
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## API

```tsx
import { MeshGradientView } from 'expo-mesh-gradient';

function App() {
  return (
    <MeshGradientView
      style={{ flex: 1 }}
      columns={3}
      rows={3}
      colors={['red', 'purple', 'indigo', 'orange', 'white', 'blue', 'yellow', 'green', 'cyan']}
      points={[
        [0.0, 0.0],
        [0.5, 0.0],
        [1.0, 0.0],
        [0.0, 0.5],
        [0.5, 0.5],
        [1.0, 0.5],
        [0.0, 1.0],
        [0.5, 1.0],
        [1.0, 1.0],
      ]}
    />
  );
}
```

## Component

### `MeshGradientView`

Supported platforms: Android, iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[MeshGradientViewProps](#meshgradientviewprops)\>

MeshGradientViewProps

### `colors`

Supported platforms: Android, iOS, tvOS.

Optional • Type: [ColorValue[]](https://reactnative.dev/docs/colors) • Default: `[]`

An array of colors. Must contain `columns * rows` elements.

### `columns`

Supported platforms: Android, iOS, tvOS.

Optional • Type: `number` • Default: `0`

Width of the mesh, i.e. the number of vertices per row.

### `ignoresSafeArea`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `true`

Whether to ignore safe areas when positioning the view.

### `mask`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `false`

Masks the gradient using the alpha channel of the given children views.

> **Note**: When this option is enabled, all user interactions (gestures) on children views are ignored.

### `points`

Supported platforms: Android, iOS, tvOS.

Optional • Type: `number[][]` • Default: `[]`

An array of two-dimensional points on the mesh. Must contain `columns * rows` elements.

### `resolution`

Supported platforms: Android.

Optional • Type: `{ x: number, y: number }`

Specifies how many points to sample on the path between points.

### `rows`

Supported platforms: Android, iOS, tvOS.

Optional • Type: `number` • Default: `0`

Height of the mesh, i.e. the number of vertices per column.

### `smoothsColors`

Supported platforms: Android, iOS, tvOS.

Optional • Type: `boolean` • Default: `true`

Whether cubic (smooth) interpolation should be used for the colors in the mesh rather than only for the shape of the mesh.

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)
