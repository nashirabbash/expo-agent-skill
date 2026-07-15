---
title: "Carousel"
description: "Jetpack Compose Carousel components for displaying scrollable collections of items."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/carousel.md"
scraped_at: "2026-07-15T09:00:33.058023"
---

---
title: Carousel
description: Jetpack Compose Carousel components for displaying scrollable collections of items.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Carousel

Jetpack Compose Carousel components for displaying scrollable collections of items.
Android, Included in Expo Go

Expo UI provides three carousel components matching the official Jetpack Compose [Carousel](https://developer.android.com/develop/ui/compose/components/carousel) API: `HorizontalCenteredHeroCarousel`, `HorizontalMultiBrowseCarousel`, and `HorizontalUncontainedCarousel`.

> **Note:** Carousel is a horizontally scrollable component, so the parent `Host` must provide a finite width on the scroll axis. Use `matchContents={{ vertical: true }}` together with `style={{ width: '100%' }}` (or any finite width). See [Match contents in Host reference](/versions/latest/sdk/ui/jetpack-compose/host.md#match-contents) for details.

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

### HorizontalCenteredHeroCarousel

Centers one large hero item between two small peek items — ideal for spotlighting content like movie posters.

```tsx
import { Host, HorizontalCenteredHeroCarousel, Box, Text } from '@expo/ui/jetpack-compose';
import { size, background } from '@expo/ui/jetpack-compose/modifiers';

export default function CenteredHeroExample() {
  const colors = ['#6200EE', '#03DAC5', '#FF5722', '#4CAF50', '#2196F3'];

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <HorizontalCenteredHeroCarousel itemSpacing={8}>
        {colors.map((color, index) => (
          <Box
            key={index}
            contentAlignment="center"
            modifiers={[size(300, 200), background(color)]}>
            <Text color="#FFFFFF">Slide {index + 1}</Text>
          </Box>
        ))}
      </HorizontalCenteredHeroCarousel>
    </Host>
  );
}
```

### HorizontalMultiBrowseCarousel

Shows a large item alongside smaller peek items, letting users browse what comes next.

```tsx
import { Host, HorizontalMultiBrowseCarousel, Box, Text } from '@expo/ui/jetpack-compose';
import { size, background } from '@expo/ui/jetpack-compose/modifiers';

export default function MultiBrowseExample() {
  const colors = ['#6200EE', '#03DAC5', '#FF5722', '#4CAF50', '#2196F3'];

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <HorizontalMultiBrowseCarousel
        preferredItemWidth={200}
        itemSpacing={8}
        flingBehavior="singleAdvance">
        {colors.map((color, index) => (
          <Box
            key={index}
            contentAlignment="center"
            modifiers={[size(200, 180), background(color)]}>
            <Text color="#FFFFFF">Card {index + 1}</Text>
          </Box>
        ))}
      </HorizontalMultiBrowseCarousel>
    </Host>
  );
}
```

### HorizontalUncontainedCarousel

Each item has a fixed width with free-form scrolling.

```tsx
import { Host, HorizontalUncontainedCarousel, Box, Text } from '@expo/ui/jetpack-compose';
import { size, background } from '@expo/ui/jetpack-compose/modifiers';

export default function UncontainedExample() {
  const items = ['Photo 1', 'Photo 2', 'Photo 3', 'Photo 4', 'Photo 5'];

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <HorizontalUncontainedCarousel
        itemWidth={160}
        itemSpacing={12}
        contentPadding={{ start: 16, top: 0, end: 16, bottom: 0 }}>
        {items.map(item => (
          <Box
            key={item}
            contentAlignment="center"
            modifiers={[size(160, 180), background('#3F51B5')]}>
            <Text color="#FFFFFF">{item}</Text>
          </Box>
        ))}
      </HorizontalUncontainedCarousel>
    </Host>
  );
}
```

## API

```tsx
import {
  HorizontalCenteredHeroCarousel,
  HorizontalMultiBrowseCarousel,
  HorizontalUncontainedCarousel,
} from '@expo/ui/jetpack-compose';
```

## Components

### `HorizontalCenteredHeroCarousel`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[HorizontalCenteredHeroCarouselProps](#horizontalcenteredherocarouselprops)\>\>

A hero carousel that centers one large item between two small peek items, matching Compose's `HorizontalCenteredHeroCarousel`.

Shared props across all carousel components.

HorizontalCenteredHeroCarouselProps

### `maxItemWidth`

Supported platforms: Android.

Optional • Type: `number`

Maximum width of the hero item in dp. When unspecified, the hero item will be as wide as possible.

### `maxSmallItemWidth`

Supported platforms: Android.

Optional • Type: `number` • Default: `CarouselDefaults.MaxSmallItemSize`

Maximum width of small peek items in dp.

### `minSmallItemWidth`

Supported platforms: Android.

Optional • Type: `number` • Default: `CarouselDefaults.MinSmallItemSize`

Minimum width of small peek items in dp.

#### Inherited Props

-   [CarouselCommonConfig](#carouselcommonconfig)

### `HorizontalMultiBrowseCarousel`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[HorizontalMultiBrowseCarouselProps](#horizontalmultibrowsecarouselprops)\>\>

A carousel that shows a large item alongside smaller peek items, matching Compose's `HorizontalMultiBrowseCarousel`.

Shared props across all carousel components.

HorizontalMultiBrowseCarouselProps

### `maxSmallItemWidth`

Supported platforms: Android.

Optional • Type: `number` • Default: `CarouselDefaults.MaxSmallItemSize`

Maximum width of small peek items in dp.

### `minSmallItemWidth`

Supported platforms: Android.

Optional • Type: `number` • Default: `CarouselDefaults.MinSmallItemSize`

Minimum width of small peek items in dp.

### `preferredItemWidth`

Supported platforms: Android.

Type: `number`

The preferred width of the large item in dp.

#### Inherited Props

-   [CarouselCommonConfig](#carouselcommonconfig)

### `HorizontalUncontainedCarousel`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[HorizontalUncontainedCarouselProps](#horizontaluncontainedcarouselprops)\>\>

A carousel where each item has a fixed width with free-form scrolling, matching Compose's `HorizontalUncontainedCarousel`.

Shared props across all carousel components.

HorizontalUncontainedCarouselProps

### `itemWidth`

Supported platforms: Android.

Type: `number`

The width of each item in dp.

#### Inherited Props

-   [CarouselCommonConfig](#carouselcommonconfig)

## Types

### `CarouselCommonConfig`

Supported platforms: Android.

Shared props across all carousel components.

| Property | Type | Description |
| --- | --- | --- |
| children | `React.ReactNode` | Children to render as carousel items. |
| contentPadding(optional) | number | [PaddingValuesRecord](#paddingvaluesrecord) | Padding for carousel content (dp or object). |
| flingBehavior(optional) | [FlingBehaviorType](#flingbehaviortype) | Controls snapping behavior when the user flings the carousel. `'singleAdvance'` snaps to the next item, `'noSnap'` allows free scrolling. |
| itemSpacing(optional) | `number` | Spacing between items in dp. Default: `0` |
| modifiers(optional) | `ModifierConfig[]` | Modifiers for the component. |
| userScrollEnabled(optional) | `boolean` | Whether the user can scroll the carousel. Default: `true` |

### `FlingBehaviorType`

Supported platforms: Android.

Literal Type: `string`

Fling behavior type for controlling carousel snapping.

Acceptable values are: `'singleAdvance'` | `'noSnap'`

### `PaddingValuesRecord`

Supported platforms: Android.

Per-side padding values in dp for the content.

| Property | Type | Description |
| --- | --- | --- |
| bottom(optional) | `number` | - |
| end(optional) | `number` | - |
| start(optional) | `number` | - |
| top(optional) | `number` | - |
