---
title: "PagerView"
description: "A horizontally paged view compatible with react-native-pager-view."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/drop-in-replacements/pagerview.md"
scraped_at: "2026-07-15T08:45:55.104416"
---

---
title: PagerView
description: A horizontally paged view compatible with react-native-pager-view.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# PagerView

A horizontally paged view compatible with react-native-pager-view.
Android, iOS

A `PagerView` component with an API compatible with `react-native-pager-view`. It wraps the platform-specific `@expo/ui` primitives: Jetpack Compose `HorizontalPager` on Android and a paged SwiftUI `ScrollView` on iOS. Each child becomes a separate page and stretches to fill the pager.

If you need lower-level control over platform-specific paging behavior or modifiers, use the native primitives directly. On iOS, [`TabView`](/versions/latest/sdk/ui/swift-ui/tabview.md#page-indicator-dots) with the `page` style also renders a horizontal pager and may fit better when you want SwiftUI's built-in page indicators.

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

Optionally, install [`react-native-worklets`](https://docs.swmansion.com/react-native-worklets/) if you need either of the following:

-   **Animated `setPage` on iOS.** Without worklets, iOS `setPage` falls back to a non-animated jump. Android animates regardless.
-   **Per-frame `onPageScroll` callbacks that stay on the UI thread.** When your `onPageScroll` handler is itself a worklet, it runs synchronously on the UI thread every frame instead of hopping to JS. Without worklets the callback still fires — it just runs on the JS thread.

## Migrating from `react-native-pager-view`

Update the import statement by importing `PagerView` from `@expo/ui/community/pager-view`:

```tsx
import PagerView from 'react-native-pager-view';
// becomes:
import PagerView from '@expo/ui/community/pager-view';
```

Before you swap, you should know what changes:

-   `orientation="vertical"`, `keyboardDismissMode`, `overdrag`, and `overScrollMode` are not supported.
-   The `usePagerView` hook is not provided — use a `ref` instead.
-   On iOS, `onPageScroll` and `onPageScrollStateChanged` only fire on iOS 18+.

See [Platform behavior](/versions/latest/sdk/ui/drop-in-replacements/pagerview.md#platform-behavior) for the full list.

## Basic usage

```tsx
import { useRef } from 'react';
import { Button, StyleSheet, Text, View } from 'react-native';
import PagerView, { type PagerViewRef } from '@expo/ui/community/pager-view';

export default function PagerViewExample() {
  const pagerRef = useRef<PagerViewRef>(null);

  return (
    <View style={{ flex: 1 }}>
      <PagerView
        ref={pagerRef}
        style={{ flex: 1 }}
        initialPage={0}
        onPageSelected={event => {
          console.log('selected page', event.nativeEvent.position);
        }}>
        <View key="one" style={[styles.page, { backgroundColor: '#fde68a' }]}>
          <Text>Page one</Text>
        </View>
        <View key="two" style={[styles.page, { backgroundColor: '#bfdbfe' }]}>
          <Text>Page two</Text>
        </View>
        <View key="three" style={[styles.page, { backgroundColor: '#bbf7d0' }]}>
          <Text>Page three</Text>
        </View>
      </PagerView>

      <Button title="Go to page 2" onPress={() => pagerRef.current?.setPage(1)} />
    </View>
  );
}

const styles = StyleSheet.create({
  page: { flex: 1, alignItems: 'center', justifyContent: 'center' },
});
```

## Platform behavior

Web is not supported and rendering `PagerView` on web throws at runtime.

| Feature | Android | iOS |
| --- | --- | --- |
| Minimum platform version | Any supported version | iOS 17+ for paging. On iOS 16, the view scrolls horizontally but pages don't snap |
| `onPageScroll` / `onPageScrollStateChanged` | ✓ | iOS 18+ only. On iOS 17, they never fire and the component logs a development warning on mount |
| Animated `setPage` | Native pager animation | Routes through `react-native-worklets`. Falls back to a non-animated jump if the package is not installed |
| `layoutDirection` | ✓ | ✗ |
| `offscreenPageLimit` | ✓ | ✗ |
| `pageMargin` | ✓ | ✗ |

Additional differences from upstream `react-native-pager-view`:

-   `orientation="vertical"`, `keyboardDismissMode`, `overdrag`, and `overScrollMode` are not supported. Only horizontal paging is available, and the others fall back to the platform pager's defaults.
-   The `usePagerView` hook is not provided. Use a `ref` to `PagerView` to access `setPage`, `setPageWithoutAnimation`, and `setScrollEnabled`.
-   `setScrollEnabled` triggers a re-render so the new value flows through to the native view as a prop. It is still useful for toggling from non-React contexts such as a ref-based gesture handler.
-   The `borderRadius` style applies on both platforms. On Android, only numeric values clip the pager. The underlying Compose host silently drops string values such as `'50%'`.

## API

```tsx
import PagerView from '@expo/ui/community/pager-view';
```

## Component

### `PagerView`

Supported platforms: Android, iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[PagerViewProps](#pagerviewprops)\>

A drop-in replacement for `react-native-pager-view`. Renders a horizontally paged view backed by Jetpack Compose's `HorizontalPager` on Android and SwiftUI on iOS. Each child is treated as a separate page.

Props for the `PagerView` component. Compatible with `react-native-pager-view`.

PagerViewProps

### `children`

Supported platforms: Android, iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Pages of the pager. Each child is treated as a separate page and stretched to fill the pager. Each child should have a stable `key`.

### `initialPage`

Supported platforms: Android, iOS.

Optional • Type: `number` • Default: `0`

Index of the page that is initially selected. Read **once** on mount; later changes are ignored. To navigate after mount, call `ref.setPage()` or `ref.setPageWithoutAnimation()`.

### `layoutDirection`

Supported platforms: Android.

Optional • Literal type: `string` • Default: `'ltr'`

Layout direction for paging.

Acceptable values are: `'ltr'` | `'rtl'`

### `offscreenPageLimit`

Supported platforms: Android.

Optional • Type: `number`

Number of pages kept off-screen on each side of the visible page.

### `onPageScroll`

Supported platforms: Android, iOS 18.0+.

Optional • Type: (event: [PagerViewOnPageScrollEvent](#pagerviewonpagescrollevent)) => void

Fires continuously while a swipe is in progress. The event's `position` is the index of the leading visible page; `offset` is the fractional progress toward the next page in the `[0, 1)` range.

Mark this handler with `'worklet'` (requires `react-native-worklets`) to run it synchronously on the UI thread every frame.

### `onPageScrollStateChanged`

Supported platforms: Android, iOS 18.0+.

Optional • Type: (event: [PageScrollStateChangedEvent](#pagescrollstatechangedevent)) => void

Fires when the scroll state changes between `idle`, `dragging`, and `settling`.

### `onPageSelected`

Supported platforms: Android, iOS.

Optional • Type: (event: [PagerViewOnPageSelectedEvent](#pagerviewonpageselectedevent)) => void

Fires when a page is fully selected. The event's `position` is the index of the new page.

### `pageMargin`

Supported platforms: Android.

Optional • Type: `number`

Pixels of padding between pages.

### `ref`

Supported platforms: Android, iOS.

Optional • Type: Ref<[PagerViewRef](#pagerviewref)\>

Ref handle exposing imperative `setPage`, `setPageWithoutAnimation`, and `setScrollEnabled` methods.

### `scrollEnabled`

Supported platforms: Android, iOS.

Optional • Type: `boolean` • Default: `true`

Whether the user can swipe between pages.

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)

## Types

### `PagerViewOnPageScrollEvent`

Supported platforms: Android, iOS.

Type: NativeSyntheticEvent<[PagerViewOnPageScrollEventData](#pagerviewonpagescrolleventdata)\>

### `PagerViewOnPageScrollEventData`

Supported platforms: Android, iOS.

Type: [Readonly](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<{ offset: number, position: number }\>

### `PagerViewOnPageSelectedEvent`

Supported platforms: Android, iOS.

Type: NativeSyntheticEvent<[PagerViewOnPageSelectedEventData](#pagerviewonpageselectedeventdata)\>

### `PagerViewOnPageSelectedEventData`

Supported platforms: Android, iOS.

Type: [Readonly](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<{ position: number }\>

### `PagerViewRef`

Supported platforms: Android, iOS.

Ref handle for the `PagerView` component.

| Property | Type | Description |
| --- | --- | --- |
| setPage | `(selectedPage: number) => void` | Animate the pager to the given page index. Out-of-range indices are silently ignored. On iOS the animation requires `react-native-worklets`; without it, `setPage` falls back to a non-animated jump. |
| setPageWithoutAnimation | `(selectedPage: number) => void` | Jump to the given page index without an animation. |
| setScrollEnabled | `(scrollEnabled: boolean) => void` | Imperatively enable or disable user scrolling. Note: If the scrollEnabled prop is also provided, subsequent prop changes win and reset the value set imperatively. To use the imperative path exclusively, omit the prop. |

### `PageScrollStateChangedEvent`

Supported platforms: Android, iOS.

Type: NativeSyntheticEvent<[PageScrollStateChangedEventData](#pagescrollstatechangedeventdata)\>

### `PageScrollStateChangedEventData`

Supported platforms: Android, iOS.

Type: [Readonly](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<{ pageScrollState: 'idle' | 'dragging' | 'settling' }\>
