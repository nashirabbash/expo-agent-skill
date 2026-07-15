---
title: "Row"
description: "A Jetpack Compose Row component for placing children horizontally."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/row.md"
scraped_at: "2026-07-15T09:00:43.017169"
---

---
title: Row
description: A Jetpack Compose Row component for placing children horizontally.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Row

A Jetpack Compose Row component for placing children horizontally.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Row`](/versions/latest/sdk/ui/universal/row.md) — it renders the appropriate native component per platform.

Expo UI Row matches the official Jetpack Compose [Row](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Row) API and places children horizontally with configurable arrangement and alignment.

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

`Row` places children horizontally. Use `horizontalArrangement` and `verticalAlignment` to control spacing and alignment.

```tsx
import { Host, Row, Text } from '@expo/ui/jetpack-compose';
import { fillMaxWidth, height } from '@expo/ui/jetpack-compose/modifiers';

export default function RowExample() {
  return (
    <Host matchContents>
      <Row
        horizontalArrangement="spaceEvenly"
        verticalAlignment="center"
        modifiers={[fillMaxWidth(), height(60)]}>
        <Text>Item 1</Text>
        <Text>Item 2</Text>
        <Text>Item 3</Text>
      </Row>
    </Host>
  );
}
```

## API

```tsx
import { Row } from '@expo/ui/jetpack-compose';
```

## Component

### `Row`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[RowProps](#rowprops)\>

RowProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `horizontalAlignment`

Supported platforms: Android.

Optional • Type: `HorizontalAlignment`

Horizontal alignment of children.

### `horizontalArrangement`

Supported platforms: Android.

Optional • Type: `HorizontalArrangement`

Horizontal arrangement of children.

### `verticalAlignment`

Supported platforms: Android.

Optional • Type: `VerticalAlignment`

Vertical alignment of children.

### `verticalArrangement`

Supported platforms: Android.

Optional • Type: `VerticalArrangement`

Vertical arrangement of children.

#### Inherited Props

-   `PrimitiveBaseProps`
