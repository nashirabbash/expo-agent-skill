---
title: "HorizontalPager"
description: "A Jetpack Compose HorizontalPager component for swipeable pages."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/horizontalpager.md"
scraped_at: "2026-07-15T09:00:57.047127"
---

---
title: HorizontalPager
description: A Jetpack Compose HorizontalPager component for swipeable pages.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# HorizontalPager

A Jetpack Compose HorizontalPager component for swipeable pages.
Android, Included in Expo Go

Expo UI HorizontalPager matches Jetpack Compose's [HorizontalPager](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#HorizontalPager\(androidx.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function2\)) — a horizontally scrolling pager that snaps to individual pages.

`HorizontalPager` does not impose its own height — give it one with the [`height`](/versions/latest/sdk/ui/jetpack-compose/modifiers.md#heightheight) modifier or place it inside a parent with a finite height.

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

### Uncontrolled

The pager owns its scroll position natively. Use `initialPage` to pick the starting page, and listen for changes with `onCurrentPageChange` (fires mid-swipe as the snap target flips) or `onSettledPageChange` (fires only after the swipe settles).

```tsx
import { Box, Column, Host, HorizontalPager, Text } from '@expo/ui/jetpack-compose';
import { background, fillMaxSize, fillMaxWidth, height } from '@expo/ui/jetpack-compose/modifiers';
import { useState } from 'react';

export default function UncontrolledPagerExample() {
  const [currentPage, setCurrentPage] = useState(1);
  const [settledPage, setSettledPage] = useState(1);

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[fillMaxWidth()]}>
        <Text style={{ typography: 'titleLarge' }}>
          currentPage: {currentPage} · settledPage: {settledPage}
        </Text>
        <HorizontalPager
          initialPage={1}
          onCurrentPageChange={setCurrentPage}
          onSettledPageChange={setSettledPage}
          modifiers={[fillMaxWidth(), height(240)]}>
          <Page label="Page 1" color="#6200EE" />
          <Page label="Page 2" color="#03DAC5" />
          <Page label="Page 3" color="#FF5722" />
        </HorizontalPager>
      </Column>
    </Host>
  );
}

function Page({ label, color }: { label: string; color: string }) {
  return (
    <Box modifiers={[fillMaxSize(), background(color)]} contentAlignment="center">
      <Text color="#FFFFFF" style={{ typography: 'headlineLarge' }}>
        {label}
      </Text>
    </Box>
  );
}
```

### Programmatic navigation

Attach a `ref` and call `animateScrollToPage` or `scrollToPage` on it. These mirror Compose's `PagerState.animateScrollToPage` and `PagerState.scrollToPage`.

```tsx
import {
  Box,
  Button,
  Column,
  Host,
  HorizontalPager,
  type HorizontalPagerHandle,
  Row,
  Text,
} from '@expo/ui/jetpack-compose';
import { background, fillMaxSize, fillMaxWidth, height } from '@expo/ui/jetpack-compose/modifiers';
import { useRef, useState } from 'react';

const PAGE_COUNT = 5;

export default function ProgrammaticPagerExample() {
  const pagerRef = useRef<HorizontalPagerHandle>(null);
  const [page, setPage] = useState(0);

  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[fillMaxWidth()]}>
        <Text style={{ typography: 'titleLarge' }}>
          Page {page + 1} / {PAGE_COUNT}
        </Text>
        <HorizontalPager
          ref={pagerRef}
          onSettledPageChange={setPage}
          modifiers={[fillMaxWidth(), height(200)]}>
          {Array.from({ length: PAGE_COUNT }).map((_, i) => (
            <Page key={i} label={`Page ${i + 1}`} color={COLORS[i]} />
          ))}
        </HorizontalPager>
        <Row horizontalArrangement={{ spacedBy: 8 }}>
          <Button onClick={() => pagerRef.current?.animateScrollToPage(Math.max(0, page - 1))}>
            <Text>Prev</Text>
          </Button>
          <Button
            onClick={() =>
              pagerRef.current?.animateScrollToPage(Math.min(PAGE_COUNT - 1, page + 1))
            }>
            <Text>Next</Text>
          </Button>
          <Button onClick={() => pagerRef.current?.scrollToPage(0)}>
            <Text>Jump to first</Text>
          </Button>
        </Row>
      </Column>
    </Host>
  );
}

const COLORS = ['#6200EE', '#03DAC5', '#FF5722', '#4CAF50', '#2196F3'];

function Page({ label, color }: { label: string; color: string }) {
  return (
    <Box modifiers={[fillMaxSize(), background(color)]} contentAlignment="center">
      <Text color="#FFFFFF" style={{ typography: 'headlineLarge' }}>
        {label}
      </Text>
    </Box>
  );
}
```

### Page spacing and content padding

Use `pageSpacing` to add a gap between pages (visible during swipe) and `contentPadding` to inset the pager so neighboring pages peek at rest.

```tsx
import { Box, Host, HorizontalPager, Text } from '@expo/ui/jetpack-compose';
import { background, fillMaxSize, fillMaxWidth, height } from '@expo/ui/jetpack-compose/modifiers';

export default function PagerLayoutExample() {
  return (
    <Host matchContents={{ vertical: true }} style={{ width: '100%' }}>
      <HorizontalPager
        pageSpacing={12}
        contentPadding={{ start: 32, end: 32 }}
        modifiers={[fillMaxWidth(), height(180)]}>
        <Page label="Page 1" color="#6200EE" />
        <Page label="Page 2" color="#03DAC5" />
        <Page label="Page 3" color="#FF5722" />
      </HorizontalPager>
    </Host>
  );
}

function Page({ label, color }: { label: string; color: string }) {
  return (
    <Box modifiers={[fillMaxSize(), background(color)]} contentAlignment="center">
      <Text color="#FFFFFF" style={{ typography: 'headlineLarge' }}>
        {label}
      </Text>
    </Box>
  );
}
```

## API

```tsx
import { HorizontalPager } from '@expo/ui/jetpack-compose';
```

## Component

### `HorizontalPager`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[HorizontalPagerProps](#horizontalpagerprops)\>

A horizontally scrolling pager that snaps to individual pages, matching Compose's `HorizontalPager`.

HorizontalPagerProps

### `beyondViewportPageCount`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

Number of pages to compose and keep beyond the visible viewport.

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children to render as pages.

### `contentPadding`

Supported platforms: Android.

Optional • Literal type: `union` • Default: `0`

Padding for pager content (dp or per-side object).

Acceptable values are: `number` | [PaddingValuesRecord](#paddingvaluesrecord)

### `initialPage`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

Page to mount on. Mirrors `rememberPagerState(initialPage = …)`. Subsequent changes have no effect — use the ref methods to navigate after mount.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onCurrentPageChange`

Supported platforms: Android.

Optional • Type: `(page: number) => void`

Fires when Compose's `PagerState.currentPage` changes — i.e. when the page closest to the snap position flips, including mid-swipe as the user crosses between pages.

### `onDragInteraction`

Supported platforms: Android.

Optional • Type: (kind: [HorizontalPagerDragInteraction](#horizontalpagerdraginteraction)) => void

Fires for each drag interaction emitted by `PagerState.interactionSource`. Combine with `onScrollInProgressChange` to distinguish user dragging from fling/snap-settling.

### `onPageScroll`

Supported platforms: Android.

Optional • Type: `(currentPage: number, currentPageOffsetFraction: number) => void`

Fires continuously while a swipe is in progress. Mirrors Compose's `PagerState.currentPage` and `currentPageOffsetFraction` — the latter is the signed fractional offset from `currentPage`, in the `[-0.5, 0.5]` range.

If the callback is marked with the `'worklet'` directive, it runs synchronously on the UI thread; otherwise it is delivered asynchronously as a regular JS event.

### `onScrollInProgressChange`

Supported platforms: Android.

Optional • Type: `(isScrollInProgress: boolean) => void`

Fires when Compose's `PagerState.isScrollInProgress` toggles — true while the pager is being dragged or animating to a snap target, false once it has settled.

### `onSettledPageChange`

Supported platforms: Android.

Optional • Type: `(page: number) => void`

Fires when Compose's `PagerState.settledPage` changes — i.e. after a swipe or programmatic scroll has fully settled.

### `pageSpacing`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

Spacing between pages in dp.

### `ref`

Supported platforms: Android.

Optional • Type: Ref<[HorizontalPagerHandle](#horizontalpagerhandle)\>

Imperative handle for programmatic navigation. Mirrors the methods on Compose's `PagerState`.

### `reverseLayout`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Whether to reverse the layout direction.

### `userScrollEnabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the user can scroll the pager by swiping.

## Types

### `HorizontalPagerDragInteraction`

Supported platforms: Android.

Literal Type: `string`

Kind of drag interaction reported by `onDragInteraction`. Mirrors Compose's `DragInteraction.Start` / `DragInteraction.Stop` / `DragInteraction.Cancel`.

Acceptable values are: `'start'` | `'stop'` | `'cancel'`

### `HorizontalPagerHandle`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| animateScrollToPage | (page: number) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Mirrors Compose's `PagerState.animateScrollToPage`. Resolves when the animation completes. |
| scrollToPage | (page: number) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Mirrors Compose's `PagerState.scrollToPage`. Jumps without animation. |

### `PaddingValuesRecord`

Supported platforms: Android.

Per-side padding values in dp for the content.

| Property | Type | Description |
| --- | --- | --- |
| bottom(optional) | `number` | - |
| end(optional) | `number` | - |
| start(optional) | `number` | - |
| top(optional) | `number` | - |
