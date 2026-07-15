---
title: "Card"
description: "A Jetpack Compose Card component for displaying content in a styled container."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/card.md"
scraped_at: "2026-07-15T09:00:37.240093"
---

---
title: Card
description: A Jetpack Compose Card component for displaying content in a styled container.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Card

A Jetpack Compose Card component for displaying content in a styled container.
Android, Included in Expo Go

Expo UI Card matches the official Jetpack Compose [Card API](https://developer.android.com/develop/ui/compose/components/card) and displays content inside a styled surface container with optional elevation and outline. The `Card` component renders a [filled card](https://developer.android.com/develop/ui/compose/components/card#filled), while `ElevatedCard` and `OutlinedCard` provide raised and bordered variants respectively.

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

### Basic card

```tsx
import { Host, Card, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function BasicCardExample() {
  return (
    <Host matchContents>
      <Card>
        <Text modifiers={[paddingAll(16)]}>This is a basic card with default styling.</Text>
      </Card>
    </Host>
  );
}
```

### Card types

Use `Card` (filled), `ElevatedCard`, or `OutlinedCard` for different styles.

```tsx
import { Host, Card, ElevatedCard, OutlinedCard, Text, Column } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function CardTypesExample() {
  return (
    <Host matchContents>
      <Column verticalArrangement={{ spacedBy: 12 }}>
        <Card>
          <Text modifiers={[paddingAll(16)]}>Filled card</Text>
        </Card>
        <ElevatedCard>
          <Text modifiers={[paddingAll(16)]}>Elevated card</Text>
        </ElevatedCard>
        <OutlinedCard>
          <Text modifiers={[paddingAll(16)]}>Outlined card</Text>
        </OutlinedCard>
      </Column>
    </Host>
  );
}
```

### Custom elevation

Use the `elevation` prop (in dp) to control shadow depth. Elevation is most meaningful on `ElevatedCard`, which uses shadow elevation. Filled `Card` uses tonal elevation by default, so changes may be subtle.

```tsx
import { Host, ElevatedCard, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function ElevatedCardExample() {
  return (
    <Host matchContents>
      <ElevatedCard elevation={8}>
        <Text modifiers={[paddingAll(16)]}>Card with 8dp elevation</Text>
      </ElevatedCard>
    </Host>
  );
}
```

### Custom border

`Card` and `OutlinedCard` accept a `border` prop to customize stroke width and color.

```tsx
import { Host, OutlinedCard, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function OutlinedCardExample() {
  return (
    <Host matchContents>
      <OutlinedCard border={{ width: 2, color: '#6200EE' }}>
        <Text modifiers={[paddingAll(16)]}>Card with custom purple border</Text>
      </OutlinedCard>
    </Host>
  );
}
```

## API

```tsx
import { Card, ElevatedCard, OutlinedCard } from '@expo/ui/jetpack-compose';
```

## Components

### `Card`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[CardProps](#cardprops)\>\>

A card component that renders a filled card surface for content.

CardProps

### `border`

Supported platforms: Android.

Optional • Type: [CardBorder](#cardborder)

Border configuration for the card.

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to display inside the card.

### `colors`

Supported platforms: Android.

Optional • Type: [CardColors](#cardcolors)

Colors for card's core elements.

### `elevation`

Supported platforms: Android.

Optional • Type: `number`

Default elevation in dp.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `ElevatedCard`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[ElevatedCardProps](#elevatedcardprops)\>\>

An elevated card component that provides a raised surface for content.

ElevatedCardProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to display inside the card.

### `colors`

Supported platforms: Android.

Optional • Type: [CardColors](#cardcolors)

Colors for card's core elements.

### `elevation`

Supported platforms: Android.

Optional • Type: `number`

Default elevation in dp. Material 3 default is 1dp.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `OutlinedCard`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[OutlinedCardProps](#outlinedcardprops)\>\>

An outlined card component that provides a bordered surface for content.

OutlinedCardProps

### `border`

Supported platforms: Android.

Optional • Type: [CardBorder](#cardborder)

Border configuration for the outlined card.

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to display inside the card.

### `colors`

Supported platforms: Android.

Optional • Type: [CardColors](#cardcolors)

Colors for card's core elements.

### `elevation`

Supported platforms: Android.

Optional • Type: `number`

Default elevation in dp.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

## Types

### `CardBorder`

Supported platforms: Android.

Border configuration for cards.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Border color. |
| width(optional) | `number` | Border width in dp. Default: `1` |

### `CardColors`

Supported platforms: Android.

Colors for card's core elements.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| contentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
